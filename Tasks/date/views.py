from datetime import date

from django.shortcuts import render
from rest_framework import generics
from .serializer import AgeSerializer
from .models import date
from rest_framework.response import Response
from datetime import date
import datetime
# Create your views here.
class postview(generics.GenericAPIView):
    serializer_class = AgeSerializer

    def post(self,request):
        today = date.today()
        date1 = request.data.get('date1')
        date2 = request.data.get('date2')

        date1 = datetime.datetime.strptime(str(date1), '%Y-%m-%d').date()
        date2 = datetime.datetime.strptime(str(date2), '%Y-%m-%d').date()
        age = date1.year-date2.year
        return Response({
            'result':age
        })

