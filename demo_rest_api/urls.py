from django.urls import path
from .views import DemoRestApi, DemoRestApiItem

urlpatterns = [
    path('', DemoRestApi.as_view(), name='demo-api-list'),
    path('<str:id>/', DemoRestApiItem.as_view(), name='demo-api-item'),
]
