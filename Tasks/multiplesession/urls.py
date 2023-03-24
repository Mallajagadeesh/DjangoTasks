from django.shortcuts import render
from django.urls import path
from .views import robo,setsession,getsession

urlpatterns = [
    path('register2/',robo),
    path('set2/',setsession),
    path('get2/',getsession),


]