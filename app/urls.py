from app.api import *
from rest_framework import routers

router = routers.DefaultRouter()

router.register('api/user', UserViewSet, 'user')


urlpatterns = router.urls