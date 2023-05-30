from django import views
from rest_framework import routers
from app.api import *
from app.views import *
from django.urls import path

urlpatterns = [
    path('api/country', Country.as_view(), name = 'country'),
    path('api/department', Department.as_view(), name = 'department'),
    path('api/city', City.as_view(), name = 'city'),
    path('api/user', User.as_view(), name = 'user'),
    path('api/office', Office.as_view(), name = 'office'),
    path('api/engagement', Engagement.as_view(), name = 'engagement'),
    path('api/service', Service.as_view(), name = 'service'),
    path('api/state', State.as_view(), name = 'state'),
    path('api/update', Update.as_view(), name = 'update'),
    path('register', UserRegister.as_view(), name = 'register'),
    path('login', UserLogin.as_view(), name = 'login'),
    path('logout', UserLogout.as_view(), name = 'logout'),
    path('user', UserView.as_view(), name = 'user')
]