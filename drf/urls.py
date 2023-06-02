"""
URL configuration for drf project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
from app.views import *
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('logout/', UserLogout.as_view(), name = 'logout'),
    path('api/user/<int:pk>/', get_user, name="get_user"),
    path('api/office/<int:pk>/', get_office, name="get_user"),
    path('api/user_offices/<int:pk>/', get_user_offices, name="user_offices"),
    path('api/user_messengers/<int:pk>/', get_user_messengers, name="get_user_messengers"),

]
