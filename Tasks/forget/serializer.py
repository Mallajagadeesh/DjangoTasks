from rest_framework import serializers
from .models import contact
class Contactserializer(serializers.ModelSerializer):
    class Meta:
        model = contact
        fields = '__all__'
