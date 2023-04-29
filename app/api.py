from rest_framework import viewsets, permissions

from .models import Cliente, Mensajero, Sucursal, Ciudad
from .serializers import ClienteSerializer, MensajeroSerializer, SucursalSerializer, CiudadSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ClienteSerializer

class MensajeroViewSet(viewsets.ModelViewSet):
    queryset = Mensajero.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = MensajeroSerializer

class SucursalViewSet(viewsets.ModelViewSet):
    queryset = Sucursal.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = SucursalSerializer

class CiudadViewSet(viewsets.ModelViewSet):
    queryset = Ciudad.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CiudadSerializer