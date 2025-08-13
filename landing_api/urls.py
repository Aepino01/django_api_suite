from django.urls import path
from .views import LandingAPI

app_name = "landing_api"
urlpatterns = [
    path("index/", LandingAPI.as_view(), name="index"),
]

