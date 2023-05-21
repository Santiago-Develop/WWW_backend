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
    id_country = serializers.CharField(source = 'id_country.name')
    class Meta:
        model = Department
        fields = (
            'id',
            'name',
            'id_country'
        )


class CitySerializer(serializers.ModelSerializer):
    id_department = serializers.CharField(source = 'id_department.name')
    class Meta:
        model = City
        fields = (
            'id',
            'name',
            'id_department'
        )


class UserSerializer(serializers.ModelSerializer):
    id_country = serializers.CharField(source = 'id_country.name')
    id_department = serializers.CharField(source = 'id_department.name')
    id_city = serializers.CharField(source = 'id_city.name')
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'password',
            'documentType',
            'documentNumber',
            'phone',
            'urlImg',
            'email',
            'role',
            'id_country',
            'id_department',
            'id_city'
        )

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        updated_user = super().update(instance, validated_data)
        updated_user.set_password(validated_data['password'])
        updated_user.save()
        return updated_user

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('role','urlImg','first_name','last_name', 'id')

class OfficeSerializer(serializers.ModelSerializer):
    id_customer = serializers.CharField(source = 'id_customer.username')
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
    id_customer = serializers.CharField(source = 'id_customer.username')
    id_messager = serializers.CharField(source = 'id_messager.username')
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