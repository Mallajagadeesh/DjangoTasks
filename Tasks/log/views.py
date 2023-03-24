from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from rest_framework import generics
from rest_framework.response import Response
from .serializer import *


class datamodel(generics.GenericAPIView):
    serializer_class = loggingSerializer

    def post(self, request):
        a = loggingSerializer(data=request.data)
        a.is_valid()
        user = a.save()
        return Response((a).data)

