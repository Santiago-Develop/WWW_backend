from django.forms import ValidationError
from app.models import *
from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class OfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Office
        fields = '__all__'

class EngagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Engagement
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    source_office = serializers.StringRelatedField()
    destination_office = serializers.StringRelatedField()

    class Meta:
        model = Service
        fields = '__all__'

class ServiceWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'


class UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Update
        fields = '__all__'


UserModel = get_user_model()


class UserRegisterSerializer(serializers.ModelSerializer):
    country = serializers.StringRelatedField()
    department = serializers.StringRelatedField()
    city = serializers.StringRelatedField()

    class Meta:
        model = UserModel
        fields = '__all__'

    def create(self, clean_data):
        user_obj = UserModel.objects.create_user(
            email=clean_data['email'],
            password=clean_data['password'],
            phone=clean_data['phone'],
            username=clean_data['username'],
            documentType=clean_data['documentType'],
            documentNumber=clean_data['documentNumber'],
            urlImg=clean_data['urlImg'],
            role=clean_data['role'],
            country=clean_data['country'],
            department=clean_data['department'],
            city=clean_data['city'],
            is_staff=True,
            is_activate=True,
            is_superuser=clean_data['is_superuser'],
        )
        user_obj.save()
        return user_obj


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def check_user(self, clean_data):
        user = authenticate(
            email=clean_data['email'], password=clean_data['password'])
        
        user_info = UserModel.objects.get(email=clean_data['email'])
        
        if not user:
            raise ValidationError('user not found')
        return user_info


class UserSerializer(serializers.ModelSerializer):
    country = serializers.StringRelatedField()
    department = serializers.StringRelatedField()
    city = serializers.StringRelatedField()

    class Meta:
        model = UserModel
        fields = '__all__'
