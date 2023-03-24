from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics, request
from rest_framework.response import Response
from knox.models import AuthToken
from .serializer import *
from django.contrib.auth import login
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
# Create your views here.
class file(generics.GenericAPIView):
    serializer_class = EmployeSerializer
    def post(self, request):
        a = EmployeSerializer(data=request.data)
        a.is_valid(raise_exception=True)
        n = a.save()
        return Response({
            "user": EmployeSerializer(n, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(n)[1]
        })

class loginview(generics.GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        value = AuthTokenSerializer(data=request.data)
        value.is_valid(raise_exception=True)
        user = value.validated_data['user']
        login(request, user)
        return Response(UserSerializer(user).data)