from app.models import *
from rest_framework import serializers


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
            'id_country',
            'id_department',
            'id_city',
        )
