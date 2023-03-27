from django.urls import reverse
from faker import Faker
from rest_framework.test import APITestCase

from accounts.models import CustomUser


class TestSetUp(APITestCase):
    def setUp(self):
        self.sign_up_url = reverse("sign-up")
        self.verify_update_url = reverse("verify-update")
        self.otp_url = reverse("otp")
        self.fake = Faker()

        self.user = CustomUser.objects.create(
            name=self.fake.name(),
            mobile_number=self.fake.phone_number(),
            is_verified=True,
        )
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()
