from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from .serializer import timesSerializer
from .models import times
from rest_framework import generics
# Create your views here.
class password(generics.GenericAPIView):
    serializer_class = timesSerializer

    def post(self,request):
            ser = timesSerializer(data=request.data)
            ser.is_valid()
            s = ser.save()
            return Response(timesSerializer(s).data)


