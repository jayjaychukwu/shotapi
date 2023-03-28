from django.test import TestCase

from ratings.models import ImageRating
from ratings.tests.test_setup import TestSetUp


class ImageRatingTestCase(TestSetUp):
    def test_image_rating_creation(self):
        self.assertEqual(self.rating.user, self.user)
        self.assertEqual(self.rating.image_url, self.image_dummy_url)
        self.assertTrue(self.rating.is_accepted)

    def test_image_rating_ordering(self):
        rating2 = ImageRating.objects.create(
            user=self.user,
            image_url=self.image_dummy_url + "1",
            is_accepted=False,
            name=self.fake.random_letters()[:5],
        )
        rating3 = ImageRating.objects.create(
            user=self.user,
            image_url=self.image_dummy_url + "2",
            is_accepted=False,
            name=self.fake.random_letters()[:5],
        )

        ratings = ImageRating.objects.all()
        self.assertEqual(list(ratings), [rating3, rating2, self.rating])
