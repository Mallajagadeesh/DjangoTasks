from django.http import HttpResponse

from .models import details
from rest_framework import serializers
class ormSerializer(serializers.ModelSerializer):
    class Meta:
        model = details
        fields = ['username','password','contact']




