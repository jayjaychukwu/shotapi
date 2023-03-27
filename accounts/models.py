from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    name = models.CharField(max_length=255, null=True, blank=True)
    mobile_number = models.CharField(max_length=20, unique=True)
    is_verified = models.BooleanField(default=False)

    USERNAME_FIELD = "mobile_number"
