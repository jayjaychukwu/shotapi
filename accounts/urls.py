from django.urls import path

from accounts.views import SignUpAPIView, VerifyMobileNumberAndUpdateUserAPIView

urlpatterns = [
    path("sign-up", SignUpAPIView.as_view(), name="sign-up"),
    path("verify-update", VerifyMobileNumberAndUpdateUserAPIView.as_view(), name="verify-update"),
]
