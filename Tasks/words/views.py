from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from rest_framework import generics
from rest_framework.response import Response
from .serializer import *
from .models import words
class password(generics.GenericAPIView):
    serializer_class = wordsserializer

    def post(self, request):
        ser = wordsserializer(data=request.data)
        ser.is_valid()
        s = ser.save()
        return Response(wordsserializer(s).data)



