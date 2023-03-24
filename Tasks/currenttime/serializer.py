import datetime

from rest_framework import serializers
from .models import times
class timesSerializer(serializers.ModelSerializer):
    class Meta:
        model = times
        fields = ['username','email','time']

    def create(self, validated_data):
        time = datetime.datetime.now()
        print(time)
        pos = times.objects.create(username=validated_data['username'], email=validated_data['email'], time=time)
        print(pos)
        return pos


