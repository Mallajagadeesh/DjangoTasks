from django.shortcuts import render, redirect
from .serializer import appserializer
from .models import app
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.


@api_view(['Get'])
def contact_list(request):
    practice = app.objects.all()
    serializer = appserializer(practice, many=True)

    return Response(serializer.data)

@api_view(['post'])
def post_app(request):
    serializer = appserializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)

@api_view(['Get'])
def getdetails(request,id):
    contact_list = app.objects.get(id=id)
    serializer = appserializer(contact_list,many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def update(request, id):
    contact_list = app.objects.get(id=id)
    serializer = appserializer(instance=contact_list, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

@api_view(['DELETE'])
def delete(request, id):
    h = app.objects.get(id=id)
    h.delete()
    return redirect(contact_list)


