from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from rest_framework import generics
from rest_framework.response import Response
from .serializer import *
from .models import datamodel
class password(generics.GenericAPIView):
    serializer_class = datamodelserializer
    def post(self,request):
        a = datamodelserializer(data=request.data)
        a.is_valid(raise_exception=True)
        a.save()
        return Response(datamodelserializer(a).data)
