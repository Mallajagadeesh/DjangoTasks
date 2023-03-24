from .models import details
from rest_framework import serializers
class detailsserializer(serializers.ModelSerializer):
    class Meta:
        model = details
        fields = ['username','password','email']


class loginserializer(serializers.ModelSerializer):
    class Meta:
        model = details
        fields = ['username','password']