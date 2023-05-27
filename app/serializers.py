from django.forms import ValidationError
from app.models import *
from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate


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


# class UserSerializer(serializers.ModelSerializer):
#     id_country = serializers.CharField(source = 'id_country.name')
#     id_department = serializers.CharField(source = 'id_department.name')
#     id_city = serializers.CharField(source = 'id_city.name')
#     class Meta:
#         model = User
#         fields = (
#             'id',
#             'username',
#             'password',
#             'documentType',
#             'documentNumber',
#             'phone',
#             'urlImg',
#             'email',
#             'role',
#             'id_country',
#             'id_department',
#             'id_city'
#         )

#     def create(self, validated_data):
#         user = User(**validated_data)
#         user.set_password(validated_data['password'])
#         user.save()
#         return user

#     def update(self, instance, validated_data):
#         updated_user = super().update(instance, validated_data)
#         updated_user.set_password(validated_data['password'])
#         updated_user.save()
#         return updated_user

# class CustomUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('role','urlImg','first_name','last_name', 'id')

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


UserModel = get_user_model()

class UserRegisterSerializer(serializers.ModelSerializer):
    id_country = serializers.StringRelatedField()
    id_department = serializers.StringRelatedField()
    id_city = serializers.StringRelatedField()

    class Meta:
        model = UserModel
        fields = '__all__'

    def create(self, clean_data):
        user_obj = UserModel.objects.create_user(
                                                    email = clean_data['email'], 
                                                    password = clean_data['password'],
                                                    phone =  clean_data['phone'],
                                                    username = clean_data['username'],
                                                    documentType = clean_data['documentType'],
                                                    documentNumber = clean_data['documentNumber'],
                                                    urlImg = clean_data['urlImg'],
                                                    role = clean_data['role'],
                                                    id_country =  clean_data['id_country'],
                                                    id_department = clean_data['id_department'],
                                                    id_city = clean_data['id_city'],
                                                    is_staff = clean_data['is_staff'],
                                                    is_activate = clean_data['is_activate'],
                                                    is_superuser = clean_data['is_superuser'],
                                                    last_login = clean_data['last_login'],
                                                    date_joined = clean_data['date_joined']
                                                )  
        user_obj.save()
        return user_obj
    

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def check_user(self, clean_data):
        user = authenticate(email = clean_data['email'], password = clean_data['password'])
        if not user:
            raise ValidationError('user not found')
        return user
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('email', 'username')