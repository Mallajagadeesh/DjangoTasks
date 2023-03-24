from django.http import HttpResponse

from .models import many, information
from rest_framework import serializers


class manyserializer(serializers.ModelSerializer):
    class Meta:
        model = many
        fields = ['username', 'password', 'contact']


from rest_framework import serializers
class informationserializer(serializers.ModelSerializer):
    class Meta:
        model = information
        fields = ['title', 'many', 'name']
