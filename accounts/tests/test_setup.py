from django.urls import reverse
from faker import Faker
from rest_framework.test import APITestCase


class TestSetUp(APITestCase):
    def setUp(self):
        self.sign_up_url = reverse("sign-up")
        self.verify_update_url = reverse("verify-update")
        self.fake = Faker()

        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()
