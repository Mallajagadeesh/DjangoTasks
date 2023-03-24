from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from .serializer import decimalSerializer
from .models import decimal
from rest_framework import generics
# Create your views here.
class password(generics.GenericAPIView):
    serializer_class = decimalSerializer

    def post(self,request):
            ser = decimalSerializer(data=request.data)
            ser.is_valid()
            s = ser.save()
            return Response(decimalSerializer(s).data)
