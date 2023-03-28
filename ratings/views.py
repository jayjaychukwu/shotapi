from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions
from rest_framework.response import Response

from ratings.models import ImageRating
from ratings.serializers import ImageDisplaySerializer, ImageRatingSerializer


class ImageAPIView(generics.GenericAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = ImageRatingSerializer

    def get(self, request, *args, **kwargs):
        user = request.user
        image_ratings = ImageRating.objects.filter(user=user)
        already_rated_urls = [ir.image_url for ir in image_ratings]
        images = [
            {"url": "http://getdrawings.com/get-icon#one-icon-3.png", "name": "One"},
            {"url": "http://getdrawings.com/get-icon#free-shirt-icon-9.png", "name": "Two"},
            {"url": "http://getdrawings.com/get-icon#serial-number-icon-19.png", "name": "Three"},
            {"url": "http://getdrawings.com/get-icon#serial-number-icon-18.png", "name": "Four"},
            {"url": "http://getdrawings.com/get-icon#number-one-icon-17.png", "name": "Five"},
        ]

        image_list = []
        for image in images:
            if image.get("url") not in already_rated_urls:
                image_list.append(image)
                serialized_data = ImageDisplaySerializer(image_list, many=True)
                return Response({"images": serialized_data.data})

        return Response({"message": f"{user.name}, you have rated all the images. Thank You!"})

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        image_url = serializer.validated_data["image_url"]
        is_accepted = serializer.validated_data["is_accepted"]
        name = serializer.validated_data["name"]
        user = request.user
        image_rating = ImageRating.objects.create(user=user, image_url=image_url, is_accepted=is_accepted)
        message = f"{user.name}, you have {'selected' if is_accepted else 'rejected'} image {image_rating.name}"


class ImageHistoryAPIView(generics.ListAPIView):
    serializer_class = ImageRatingSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return ImageRating.objects.filter(user=user)
