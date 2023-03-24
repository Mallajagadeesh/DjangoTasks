from .models import words
from rest_framework import serializers
from num2words import num2words

def converstion(a):
    pos = num2words(a)
    return pos

class wordsserializer(serializers.ModelSerializer):
    class Meta:
        model = words
        fields = '__all__'


    def create(self,validated_data):
        currency = validated_data['currency']
        covert = converstion(currency)
        pos = words.objects.create(currency = currency,covert = covert)
        pos.save()
        return pos
