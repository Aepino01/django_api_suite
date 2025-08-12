from django.urls import path
# si estás usando la vista que guarda en Firebase:
from landing_api.views import LandingAPI  # <-- opción A (recomendada)

urlpatterns = [
    path("", LandingAPI.as_view(), name="demo_rest_api_root"),       # /demo/rest/api/
    path("index/", LandingAPI.as_view(), name="demo_rest_api_resources"),  # /demo/rest/api/index/
]
