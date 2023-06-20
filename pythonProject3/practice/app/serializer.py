from .models import app
from rest_framework import serializers

# serializer
class appserializer(serializers.ModelSerializer):
    class Meta:
        model = app
        fields = '__all__'
