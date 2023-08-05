from rest_framework import generics
from rest_framework.response import Response
from .models import *
from .serializer import appserializer,branchmodelserializer
from django.http import HttpResponse


class create(generics.GenericAPIView):
    serializer_class = appserializer

    def post(self, request):
        d = appserializer(data=request.data)
        d.is_valid(raise_exception=True)
        u = d.save()
        return Response(appserializer(u).data)

class details(generics.ListAPIView):
        queryset = app.objects.all()
        serializer_class = appserializer

class Friendsupdate(generics.UpdateAPIView):
        queryset = app
        serializer_class = appserializer

class Friendsdelete(generics.DestroyAPIView):
        queryset = app
        serializer_class = appserializer


class dommypost(generics.GenericAPIView):
    serializer_class = branchmodelserializer

    def post(self, request):
        d = branchmodelserializer(data=request.data)
        d = self.get_serializer(data=request.data)
        d.is_valid(raise_exception=True)
        j = d.save()
        # return Response()
        return Response({
            "Result": d.data,
        })


