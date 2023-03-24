from rest_framework import serializers
from .models import decimal

def calculated(n, d):
    pos=(f'%.{d}f' % n)
    return pos

class decimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = decimal
        fields = ['number','digits','decimalvalue']

    def create(self,validated_data):
        number = validated_data['number']
        digits = validated_data['digits']
        decimalvalue =calculated(number, digits)
        pos = decimal.objects.create(number = validated_data['number'],digits = validated_data['digits'], decimalvalue=decimalvalue)
        pos.save()
        return pos