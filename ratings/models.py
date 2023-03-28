from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class ImageRating(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image_url = models.CharField(max_length=255)
    is_accepted = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"{self.user.name} {'accepted' if self.is_accepted else 'rejected'} image {self.name}"
