from rest_framework import serializers

from ratings.models import ImageRating


class ImageRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageRating
        fields = "__all__"

    def validate_image_url(self, value):
        user = self.context["request"].user
        if ImageRating.objects.filter(user=user, image_url=value).exists():
            raise serializers.ValidationError("This image has already been rated.")
        return value


class ImageDisplaySerializer(serializers.Serializer):
    url = serializers.URLField()
    name = serializers.CharField()
