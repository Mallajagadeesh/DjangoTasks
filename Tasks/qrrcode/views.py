from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from rest_framework import generics
from rest_framework.response import Response
from .serializer import *
from .models import qrcode
class datamodel(generics.GenericAPIView):
    serializer_class =qrserializer
    def post(self, request):
        a = qrserializer(data=request.data)
        a.is_valid(raise_exception=True)
        user=a.save()
        return Response(qrserializer(user).data)

    # def getimage(self,request):
    #     products = qrcode.objects.all()
    #     return render(request,'read.html',{'image':products})







