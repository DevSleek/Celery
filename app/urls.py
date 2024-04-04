from django.urls import path
from app.views import HouseListAPIView

urlpatterns = [
    path('api/v1/teams/', HouseListAPIView.as_view())
]
