from django.shortcuts import render
from .models import patient
from django.http import HttpResponse
# Create your views here.
from rest_framework import generics
from rest_framework.response import Response
from .serializer import *
from .models import patient
class password(generics.GenericAPIView):
    serializer_class = patienterializer

    def post(self, request):
        serializer = patienterializer(data=request.data)
        serializer.is_valid()
        s = serializer.save()
        return Response(patienterializer(s).data)
