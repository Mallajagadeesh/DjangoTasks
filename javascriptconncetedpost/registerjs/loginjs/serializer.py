from .models import register
from rest_framework import serializers


class registerserializer(serializers.ModelSerializer):
    class Meta:
        model = register
        fields = '__all__'


class Loginserializer(serializers.ModelSerializer):
    class Meta:
        model = register
        fields = ['email_id', 'Password']
