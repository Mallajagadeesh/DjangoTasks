from rest_framework import serializers
from .models import Uploadimage


class UploadimageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Uploadimage
        fields = '__all__'
