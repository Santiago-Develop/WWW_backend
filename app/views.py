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

from app.models import *
from app.serializers import *


# class Login(ObtainAuthToken):

#     def post(self, request, *args, **kwargs):
#         login_serializer = self.serializer_class(
#             data=request.data, context={'request': request})

#         if login_serializer.is_valid():
#             user = login_serializer.validated_data['user']
#             if user.is_active:
#                 token, created = Token.objects.get_or_create(user=user)
#                 user_serializer = CustomUserSerializer(user)

#                 if not created:
#                     token.delete()
#                     token = Token.objects.create(user=user)
#                 else:
#                     return Response({
#                         'message': "Someone else has already logged in with this user",
#                     }, status=status.HTTP_400_BAD_REQUEST)

#                 return Response({
#                     'token': token.key,
#                     'user': user_serializer.data,
#                     'message': "Login successful",
#                 }, status=status.HTTP_200_OK)
#             else:
#                 return Response({
#                     'message': "This user can not log in",
#                 }, status=status.HTTP_401_UNAUTHORIZED)
#         return Response({
#             'message': "User or password incorrect",
#         }, status=status.HTTP_400_BAD_REQUEST)

class Country(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)

class Department(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)

class City(generics.ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)

# class User(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     #permission_classes = (IsAuthenticated,)
#     authentication_class = (TokenAuthentication,)

#     def get_queryset(self):
#         user = self.request.user
#         qs = super().get_queryset()
#         qs = qs.filter(id=user.id)
#         return qs

class Office(generics.ListCreateAPIView):
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)

    def get_queryset(self):
        user = self.request.user
        qs = super().get_queryset()
        if not user.is_superuser:
            qs = qs.filter(id_customer=user.id)
        return qs

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
    serializer_class =StateSerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)

class Update(generics.ListCreateAPIView):
    queryset = Update.objects.all()
    serializer_class =UpdateSerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)

class Login(FormView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('user')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login, self).dispatch(request, *args, *kwargs)
      
    def form_valid(self, form):
        user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password'])
        token,_ = Token.objects.get_or_create(user = user)
        if token:
            login(self.request, form.get_user())
            return super(Login, self).form_valid(form)
        

class Logout(APIView):
    def get(self, request, format = None):
        request.user.auth_token.delete()
        logout(request)
        return Response(status = status.HTTP_200_OK)


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
            return Response(serializer.data, status=status.HTTP_200_OK)
        

class UserLogout(APIView):
    def post (self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)
    

class UserView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response({'user': serializer.data}, status=status.HTTP_200_OK)