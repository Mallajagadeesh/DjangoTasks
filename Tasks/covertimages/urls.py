from django.shortcuts import render
from django.urls import path
from .views import images

urlpatterns = [
    path('covert/',images),
]