from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from .serializer import Contactserializer
from .models import contact
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view(['GET'])
def contact_list(request):
    contacts   = contact.objects.all()
    serializer = Contactserializer(contacts,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_contact(request):
    serializer = Contactserializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(Contactserializer(serializer).data)

# @api_view(['POST'])

class update_contact(generics.GenericAPIView):
    serializer_class = Contactserializer

    def post(request,id):
        username = request.data.get('name')
        password = request.data.get('password')
        reenterpassword = request.data.get('reenterpassword')
        if password == reenterpassword:
            contacts = contact.objects.get(name=username)
            serializer = Contactserializer(instance=contacts, data=request.data)
            if serializer.is_valid():
                serializer.save()
        else:
          return HttpResponse('worngdeatils')

        return Response(serializer.data)
