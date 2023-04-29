from app.api import ClienteViewSet, MensajeroViewSet, SucursalViewSet, CiudadViewSet
from rest_framework import routers


router = routers.DefaultRouter()

router.register('api/cliente', ClienteViewSet, 'cliente')
router.register('api/mensajero', MensajeroViewSet, 'mensajero')
router.register('api/sucursal', SucursalViewSet, 'sucursal')
router.register('api/ciudad', CiudadViewSet, 'ciudad')

urlpatterns = router.urls