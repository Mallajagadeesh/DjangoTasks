from .models import date
from rest_framework import serializers
class AgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = date
        fields = '__all__'