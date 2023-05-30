from rest_framework import viewsets, permissions

from .models import *
from .serializers import *

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CountrySerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = DepartmentSerializer

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CitySerializer

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     permission_classes = [permissions.AllowAny]
#     serializer_class = UserSerializer

class OfficeViewSet(viewsets.ModelViewSet):
    queryset = Office.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = OfficeSerializer

class EngagementViewSet(viewsets.ModelViewSet):
    queryset = Engagement.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = EngagementSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ServiceSerializer

class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = StateSerializer

class UpdateViewSet(viewsets.ModelViewSet):
    queryset = Update.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UpdateSerializer