from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from .serializer import datamodelSerializer
from .models import datamodel
from rest_framework import generics
# Create your views here.
class password(generics.GenericAPIView):
    serializer_class = datamodelSerializer

    def post(self,request):
            ser = datamodelSerializer(data=request.data)
            ser.is_valid()
            s = ser.save()
            return Response(datamodelSerializer(s).data)























# def post(request):
#     if request.method == 'POST':
#         d = datamodel()
#         d.datetime = request.POST.get('datetime')
#         d.timezone = request.POST.get('timezone')
#         d.save()
#         return HttpResponse('sucess')
#     else:
#         return HttpResponse('wrong details')
#
#

