import datetime
import pytz
from pytz import country_timezones
from .models import datamodel
from rest_framework import serializers
class datamodelSerializer(serializers.ModelSerializer):
    class Meta:
        model = datamodel
        fields = ['timezone','DateTime']

    def create(self, validated_data):
        timezne = validated_data['timezone']
        zone_time = datetime.datetime.now(pytz.timezone(timezne))
        pos =datamodel.objects.create(timezone=timezne, DateTime=zone_time)
        pos.save()
        return pos
