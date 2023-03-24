from .models import datamodel
from rest_framework import serializers
class datamodelserializer(serializers.ModelSerializer):
    class Meta:
        model = datamodel
        fields = ['username','password','gender','email']
