from rest_framework import serializers
from .models import RegisterUser


class UserRegister(serializers.ModelSerializer):
    class Meta:
        model = RegisterUser
        fields = '__all__'


class loginRegister(serializers.ModelSerializer):
    class Meta:
        model = RegisterUser
        fields = ['emailid', 'Password']
