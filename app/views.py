from django.shortcuts import render
from rest_framework import generics, permissions
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .validations import custom_validation, validate_email, validate_password
from rest_framework.decorators import api_view
from app.models import *
from app.serializers import *
from app.models import Office as OfficeModel

import json


class Country(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    authentication_class = (TokenAuthentication,)


class Department(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    authentication_class = (TokenAuthentication,)


class City(generics.ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    authentication_class = (TokenAuthentication,)


class User(generics.ListCreateAPIView):
    queryset = AppUser.objects.all()
    serializer_class = UserSerializer
    # permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)

    # def get_queryset(self):
    #     user = self.request.user
    #     qs = super().get_queryset()
    #     if not user.is_superuser:
    #         qs = qs.filter(email=user.email)
    #     return qs


class Office(generics.ListCreateAPIView):
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer
    # permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)

    # def get_queryset(self):
    #     user = self.request.user
    #     qs = super().get_queryset()
    #     if not user.is_superuser:
    #         qs = qs.filter(customer_id=user.id)
    #     return qs


class Engagement(generics.ListCreateAPIView):
    queryset = Engagement.objects.all()
    serializer_class = EngagementSerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)

    def get_queryset(self):
        user = self.request.user
        qs = super().get_queryset()
        if not user.is_superuser:
            qs = qs.filter(id_customer=user.id)
        return qs


class Service(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)


class State(generics.ListCreateAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)


class Update(generics.ListCreateAPIView):
    queryset = Update.objects.all()
    serializer_class = UpdateSerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)


class Logout(APIView):
    def get(self, request, format=None):
        request.user.auth_token.delete()
        logout(request)
        return Response(status=status.HTTP_200_OK)


class UserRegister(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        clean_data = custom_validation(request.data)
        serializers = UserRegisterSerializer(data=clean_data)
        if serializers.is_valid(raise_exception=True):
            user = serializers.create(clean_data)
            if user:
                return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class UserLogin(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (SessionAuthentication,)

    def post(self, request):
        data = request.data
        assert validate_email(data)
        assert validate_password(data)
        serializer = UserLoginSerializer(data=data)

        if serializer.is_valid(raise_exception=True):
            user = serializer.check_user(data)
            login(request, user)
            email = data.get('email')
            user_info = UserModel.objects.get(email=email)

            response = {
                "id": user_info.user_id,
                "name": user_info.username,
                "role": user_info.role,
                "urlImg": user_info.urlImg,
            }
            return Response(json.dumps(response), status=status.HTTP_200_OK)


class UserLogout(APIView):
    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)


class UserView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response({'user': serializer.data}, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_user(request, pk):
    try:
        if request.method == 'GET':
            userApp = AppUser.objects.get(user_id=pk)
            user_serializer = UserSerializer(
                userApp, many=False, context={'request': request})

            return Response(user_serializer.data)

    except:
        return Response({"error": True, "message": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'POST', 'DELETE'])
def get_office(request, pk):
    try:
        if request.method == 'GET':
            office = OfficeModel.objects.get(id=pk)
            serializer = OfficeSerializer(
                office, many=False, context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif request.method == 'POST':
            office = OfficeModel.objects.get(id=pk)
            body = json.loads(request.body.decode('utf-8'))
            name = body.get('name')
            address = body.get('address')
            phone = body.get('phone')

            if name:
                office.name = name
            if address:
                office.address = address
            if phone:
                office.phone = phone

            office.save()
            
            return Response({"message": "Office updated"}, status=status.HTTP_200_OK)
        elif request.method == 'DELETE':
            office = OfficeModel.objects.get(id=pk)
            name = office.name
            office.delete()
            return Response({"message": "Office deleted", "name": name}, status=status.HTTP_200_OK)
    except Exception as err:
        print(err)
        return Response({"error": True, "message": "Office does not exist"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_user_offices(request, pk):
    try:
        if request.method == 'GET':
            userApp = AppUser.objects.get(user_id=pk)
            offices = OfficeModel.objects.filter(customer=userApp)
            serializer = OfficeSerializer(
                offices, many=True, context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        return Response({"error": True, "message": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)
