from django.urls import path
from .views import *
urlpatterns = [
    path('impl/',datamodel.as_view()),
]