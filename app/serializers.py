from app.models import *
from rest_framework import serializers

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = (
            'id',
            'name',
        )

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = (
            'id',
            'name',
            'id_country'
        )

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = (
            'id',
            'name',
            'id_department'
        )

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'name',
            'documentType',
            'documentNumber',
            'phone',
            'urlImg',
            'email',
            'role',
            'password',
            'id_country',
            'id_department',
            'id_city'
        )

class OfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Office
        fields = (
            'id',
            'name',
            'address',
            'phone',
            'id_customer'
        )

class EngagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Engagement
        fields = (
            'id',
            'id_customer',
            'id_messager'
        )

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = (
            'id',
            'code',
            'amount',
            'transport',
            'date_time',
            'description',
            'id_customer',
            'id_messager',
            'id_source_office',
            'id_source_destination'
        )

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = (
            'id',
            'name'
        )

class UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Update
        fields = (
            'id',
            'new_state',
            'photo',
            'description',
            'current_date_time',
            'id_service',
            'id_state'
        )