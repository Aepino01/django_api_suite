#from django.urls import path
#from .views import DemoRestApi, DemoRestApiItem

#urlpatterns = [
#    path('', DemoRestApi.as_view(), name='demo-api-list'),
 #   path('<str:id>/', DemoRestApiItem.as_view(), name='demo-api-item'),
#]
from django.urls import path
from . import views

urlpatterns = [
   path("index/", views.DemoRestApi.as_view(), name="demo_rest_api_resources" ),
]
