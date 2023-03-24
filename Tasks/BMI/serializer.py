from rest_framework import serializers
from .models import patient

def calculate(h,w):
    BMI = w/(h/100)** 2
    return BMI

class patienterializer(serializers.ModelSerializer):
    class Meta:
        model = patient
        fields = ['weight','height']

    def create(self,validated_data):
        weight = validated_data['weight']
        height = validated_data['height']
        calculatebmi = calculate(height,weight)
        user = patient.objects.create(weight=weight,height=height,calculatedbmi=calculatebmi)
        user.save()
        return user

