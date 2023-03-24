from django.urls import path
from .views import *

urlpatterns = [
    path('vaild/',password.as_view()),
]
