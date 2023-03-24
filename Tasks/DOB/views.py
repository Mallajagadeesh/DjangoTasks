from datetime import date

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from rest_framework import generics
from rest_framework.response import Response
from .serializer import *
from .models import birth
class password(generics.GenericAPIView):
    serializer_class = birthserializer

    def post(self,request):
        today = date.today()
        year = today.year
        print(type(year))
        age = request.data.get('age')
        print(type(age))
        dob = int(age)-year
        return Response({
            'result':dob
        })

