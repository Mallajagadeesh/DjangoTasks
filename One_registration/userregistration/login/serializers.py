from .models import Registration
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = '__all__'


class loginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = ['Email_id', 'password']
