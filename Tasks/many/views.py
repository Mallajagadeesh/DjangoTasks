from django.shortcuts import render
from .serializer import *
#create your views here.
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import many
# Create your views here.
from rest_framework import generics
class postview(generics.GenericAPIView):
    serializer_class = informationserializer

    def post(self,request):
        serializer = informationserializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        s=serializer.save()
        return Response(informationserializer(s).data)


class getview(generics.GenericAPIView):
    queryset = informationserializer
    def get(self, request):
        var = information.objects.all()
        ser = informationserializer(var, many=True)
        return Response((ser).data)
