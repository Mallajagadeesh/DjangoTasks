from .models import birth
from rest_framework import serializers
class birthserializer(serializers.ModelSerializer):
    class Meta:
        model = birth
        fields = ['dob']

