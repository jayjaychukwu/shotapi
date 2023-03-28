from django.urls import path

from ratings.views import ImageAPIView, ImageHistoryAPIView

urlpatterns = [
    path("images/", ImageAPIView.as_view(), name="images"),
    path("image-history", ImageHistoryAPIView.as_view(), name="image-history"),
]
