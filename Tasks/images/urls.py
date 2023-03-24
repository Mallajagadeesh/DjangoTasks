from django.shortcuts import render
from django.urls import path

from .views import upload

urlpatterns = [
    path('photos/',upload),
]