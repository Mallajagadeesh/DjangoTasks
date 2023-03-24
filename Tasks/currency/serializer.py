from rest_framework import serializers
from .models import Currencysymbol
class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["country"]
        model = Currencysymbol
class GetSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Currencysymbol