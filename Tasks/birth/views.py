import datetime

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from rest_framework import generics
from rest_framework.response import Response
from .serializer import *
from .models import birth
class password(generics.GenericAPIView):
    serializer_class = birthserializer

    def post(self, request):
        today = datetime.date.today()
        dob = request.data.get('dob')
        # dob = datetime.datetime.strptime(str(dob)), '%Y-5m-%d').date()
        age = today.year-dob.year
        return Response({
            'result':age
        })

