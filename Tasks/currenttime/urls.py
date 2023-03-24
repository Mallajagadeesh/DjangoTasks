from django.urls import path
from .views import *
urlpatterns = [
     path('stamp/',password.as_view())
]


