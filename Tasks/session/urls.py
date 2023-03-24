
from django.urls import path
from .views import *
urlpatterns = [
    path('set/',setsession),
    path('get/',getsession),
    path('register/',games),
    path('login/',login),
]
