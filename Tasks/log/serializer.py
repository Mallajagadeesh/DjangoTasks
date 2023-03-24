
from .models import Logging
from rest_framework import serializers


class loggingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logging
        fields = '__all__'
