from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status
from rest_framework.response import Response

from accounts.models import CustomUser
from accounts.serializers import (
    CustomUserSerializer,
    SignInSerializer,
    SignUpSerializer,
    VerifyUpdateSerializer,
)
from accounts.utils import OTP


class SignUpAPIView(generics.GenericAPIView):
    serializer_class = SignUpSerializer

    def post(self, request, *args, **kwargs):
        # obtain the mobile number for the request data
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        mobile_number = serializer.validated_data.get("mobile_number")

        user = CustomUser.objects.filter(mobile_number=mobile_number).first()

        # here should where the mock for sending the otp occurs
        OTP.send_otp(number=mobile_number)

        if not user:
            user = CustomUser(mobile_number=mobile_number)
            user.save()

        user_serializer = CustomUserSerializer(user)

        return Response(
            {"message": "OTP has been sent to your mobile number", "data": user_serializer.data},
            status=status.HTTP_200_OK,
        )


class VerifyMobileNumberAndUpdateUserAPIView(generics.GenericAPIView):
    serializer_class = VerifyUpdateSerializer

    def post(self, request, *args, **kwargs):
        # obtain the mobile number and otp
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        mobile_number = serializer.validated_data.get("mobile_number")
        name = serializer.validated_data.get("name")
        otp = serializer.validated_data.get("otp")

        try:
            user = CustomUser.objects.get(mobile_number=mobile_number)
        except CustomUser.DoesNotExist:
            return Response({"error": "user not found"}, status=status.HTTP_400_BAD_REQUEST)

        # verify mobile number
        if otp != "00000":
            return Response({"error": "invalid OTP"}, status=status.HTTP_400_BAD_REQUEST)

        # update the user verification status
        user.is_verified = True
        user.name = name
        user.save()

        user_serializer = CustomUserSerializer(user)

        return Response(
            {"message": "successfully signed up", "data": user_serializer.data}, status=status.HTTP_201_CREATED
        )


class OTPAPIView(generics.GenericAPIView):
    serializer_class = SignUpSerializer

    @swagger_auto_schema(
        query_serializer=SignUpSerializer,
        responses={
            "200": "OK",
            "400": "Bad Request",
        },
    )
    def get(self, request):
        mobile_number = request.query_params.get("mobile_number")
        # return static OTP value
        otp = OTP.send_otp(number=mobile_number)
        return Response({"otp": otp})


class UserSignInAPIView(generics.GenericAPIView):
    serializer_class = SignInSerializer

    def post(self, request):
        # get mobile number and OTP from request data
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        mobile_number = serializer.validated_data.get("mobile_number")
        otp = serializer.validated_data.get("otp")

        # find the user with the number
        try:
            user = CustomUser.objects.get(mobile_number=mobile_number)
        except CustomUser.DoesNotExist:
            return Response({"error": "user does not exist"}, status=status.HTTP_404_BAD_REQUEST)

        if user.is_verified is False:
            return Response({"error": "user is not verified"}, status=status.HTTP_400_BAD_REQUEST)

        # verify the otp
        if otp != "00000":
            return Response(
                {"error": "invalid OTP"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        message = "Welcome " + user.name
        return Response({"message": message})
