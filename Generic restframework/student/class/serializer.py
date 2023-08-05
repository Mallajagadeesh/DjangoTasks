from .models import app, branchmodel
from rest_framework import serializers


# serializer


class appserializer(serializers.ModelSerializer):
    class Meta:
        model = app
        fields = '__all__'


class branchmodelserializer(serializers.ModelSerializer):
    class Meta:
        model = branchmodel
        fields = '__all__'
