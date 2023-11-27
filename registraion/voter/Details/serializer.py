from .models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class loginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['emailid', 'Password']
