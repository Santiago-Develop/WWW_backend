from app.models import Cliente, Mensajero, Sucursal, Ciudad
from rest_framework import serializers


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('id', 'nombre', 'direccion', 'ciudad', 'email', 'telefono')

class MensajeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mensajero
        fields = ('id', 'nombre', 'direccion', 'email', 'telefono', 'cliente_id')

class SucursalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sucursal
        fields = ('id', 'nombre', 'direccion', 'telefono', 'cliente_id')

class CiudadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ciudad
        fields = ('id', 'nombre')