"""
URL configuration for backend_data_server project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.shortcuts import redirect
from django.urls import path, include
from django.contrib import admin

def redirect_to_api(request):
    # antes redirigía a /demo/rest/api/ (que no existe)
    return redirect('/demo/rest/api/index/')

urlpatterns = [
    path("admin/", admin.site.urls),
    #path("homepage/", include("templates.homepage.urls")),
    path("homepage/", include("homepage.urls")),
    path("demo/rest/api/", include("demo_rest_api.urls")),
    path("", redirect_to_api),
]

