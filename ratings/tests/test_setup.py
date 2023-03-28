from django.urls import reverse
from faker import Faker
from rest_framework.test import APITestCase

from accounts.models import CustomUser
from ratings.models import ImageRating


class TestSetUp(APITestCase):
    def setUp(self):
        self.images_url = reverse("images")
        self.image_history_url = reverse("image-history")
        self.fake = Faker()
        self.image_dummy_url = "http://example.com/image.jpg"
        self.user = CustomUser.objects.create(
            name=self.fake.name(),
            mobile_number=self.fake.phone_number()[:20],
            is_verified=True,
        )
        self.rating = ImageRating.objects.create(
            user=self.user,
            image_url=self.image_dummy_url,
            is_accepted=True,
            name=self.fake.random_letters()[:5],
        )
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()
