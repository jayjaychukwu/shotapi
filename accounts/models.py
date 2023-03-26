from django.db import models


class CustomUser(models.Model):
    name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=20)
    is_verified = models.BooleanField(default=False)
    