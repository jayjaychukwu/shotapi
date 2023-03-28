from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from accounts.views import (
    OTPAPIView,
    SignUpAPIView,
    UserSignInAPIView,
    VerifyMobileNumberAndUpdateUserAPIView,
)

urlpatterns = [
    path("sign-up", SignUpAPIView.as_view(), name="sign-up"),
    path("verify-update", VerifyMobileNumberAndUpdateUserAPIView.as_view(), name="verify-update"),
    path("otp", OTPAPIView.as_view(), name="otp"),
    path("sign-in", UserSignInAPIView.as_view(), name="sign-in"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
