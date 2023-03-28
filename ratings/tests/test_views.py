from rest_framework import status

from ratings.tests.test_setup import TestSetUp


class ImageViewTestCase(TestSetUp):
    def test_get_image(self):
        self.client.force_login(self.user)
        response = self.client.get(self.images_url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_image(self):
        data = {
            "image_url": "http://getdrawings.com/get-icon#one-icon-3.png",
            "name": "one",
            "is_accepted": True,
            "user": self.user.id,
        }
        self.client.force_login(self.user)
        response = self.client.post(self.images_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_image_history(self):
        self.client.force_login(self.user)
        response = self.client.get(self.image_history_url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
