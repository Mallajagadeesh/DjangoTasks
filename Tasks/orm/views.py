from django.http import HttpResponse
from django.shortcuts import render
from .serializer import *
#create your views here.
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import details
# Create your views here.
from rest_framework import generics



class postview(generics.GenericAPIView):
    serializer_class = ormSerializer

    def post(self,request):
        serializer = ormSerializer(data=request.data)
        serializer.is_valid()
        s=serializer.save()
        return Response(ormSerializer(s).data)



class getview(generics.GenericAPIView):
    queryset = ormSerializer
    def get(self, request):
        var = details.objects.all()
        ser = ormSerializer(var, many=True)
        return Response((ser).data)
