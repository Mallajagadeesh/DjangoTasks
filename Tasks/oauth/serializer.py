from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password,check_password

class EmployeSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields = ('username', 'password', 'email', )
    def create(self, validated_data):
        passwd= validated_data['password']
        user = User.objects.create(username=validated_data['username'],password=make_password(passwd),email=validated_data['email'])
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','password')



