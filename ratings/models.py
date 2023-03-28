from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class ImageRating(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image_url = models.CharField(max_length=255, unique=True)
    is_accepted = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
