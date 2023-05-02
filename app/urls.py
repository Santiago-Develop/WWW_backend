from rest_framework import routers
from app.api import *
from app.views import *
from django.urls import path

router = routers.DefaultRouter()

router.register('api/country', CountryViewSet, 'country')
router.register('api/department', DepartmentViewSet, 'department')
router.register('api/city', CityViewSet, 'city')
router.register('api/user', UserViewSet, 'user')
router.register('api/office', OfficeViewSet, 'office')
router.register('api/engagement', EngagementViewSet, 'engagement')
router.register('api/service', ServiceViewSet, 'service')
router.register('api/state', StateViewSet, 'state')
router.register('api/update', UpdateViewSet, 'update')


urlpatterns = [
    path('api/login', Login.as_view()),
]

urlpatterns += router.urls
