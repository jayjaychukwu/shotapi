from rest_framework import serializers

from accounts.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["name", "is_verified", "mobile_number"]


class SignUpSerializer(serializers.Serializer):
    mobile_number = serializers.CharField(max_length=20, min_length=10, required=True)


class VerifyUpdateSerializer(serializers.Serializer):
    otp = serializers.CharField()
    mobile_number = serializers.CharField()
    name = serializers.CharField()


class SignInSerializer(serializers.Serializer):
    mobile_number = serializers.CharField()
    otp = serializers.CharField()
