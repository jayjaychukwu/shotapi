from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from accounts.models import CustomUser
from accounts.tests.test_setup import TestSetUp


class SignUpTestCase(TestSetUp):
    def test_user_sign_up_and_verification(self):
        # test user sign up
        url = self.sign_up_url
        mobile_number = self.fake.phone_number()[:20]
        data = {"mobile_number": mobile_number}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        user_id = response.data["data"]["id"]

        # test verification and update
        url = self.verify_update_url
        name = self.fake.name()
        data = {"mobile_number": mobile_number, "name": name, "otp": "00000"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(response.data["data"]["is_verified"])
        self.assertEqual(response.data["data"]["mobile_number"], mobile_number)
        self.assertEqual(response.data["data"]["name"], name)
        self.assertEqual(response.data["data"]["id"], user_id)


class OTPAPITestCase(TestSetUp):
    def test_get_otp(self):
        # Test getting otp
        url = self.otp_url
        response = self.client.get(url, {"mobile_number": self.user.mobile_number})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["otp"], "00000")


class SignInTestCase(TestSetUp):
    def test_user_sign_in(self):
        # test the user sign in
        url = self.sign_in_url
        data = {"mobile_number": self.user.mobile_number, "otp": "00000"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["message"], "Welcome " + self.user.name)

    def test_invalid_orp(self):
        # Test invalid OTP
        url = self.sign_in_url
        data = {"mobile_number": self.user.mobile_number, "otp": "00001"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["error"], "invalid OTP")

    def test_unverified_user(self):
        # Test unverified user
        self.user.is_verified = False
        self.user.save()
        url = self.sign_in_url
        data = {"mobile_number": self.user.mobile_number, "otp": "00000"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["error"], "user is not verified")
