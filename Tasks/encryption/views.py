import hashlib

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from rest_framework import generics
from rest_framework.response import Response
from .serializer import *
from .models import details
class password(generics.GenericAPIView):
    serializer_class = detailsserializer

    def post(self,request):
        a=details()
        a.username = request.POST.get('username')
        password = request.POST.get('password')
        saltpassword = hashlib.md5(password.encode())
        serializers = saltpassword.hexdigest()
        a.password = serializers
        a.email = request.POST.get('email')
        a.save()
        return Response(detailsserializer(a).data)


class login(generics.GenericAPIView):
    serializer_class = loginserializer

    def post(self,request):
        username = request.data.get('username')
        password = request.data.get('password')
        saltpassword = hashlib.md5(password.encode())
        serializers = saltpassword.hexdigest()
        d = details.objects.get(username=username)
        print(d.password)
        if d.password == serializers:
            return Response(loginserializer(d).data)
        else:
            return HttpResponse('wrong details')
