from django.shortcuts import render
from rest_framework import generics
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
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

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

class User(generics.ListCreateAPIView):
    queryset = User.objects.filter(role='CUSTOMER') | User.objects.filter(role='MESSAGER')
    serializer_class = UserSerializer
    #permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)

class Office(generics.ListCreateAPIView):
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)

class Engagement(generics.ListCreateAPIView):
    queryset = Engagement.objects.all()
    serializer_class = EngagementSerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)

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