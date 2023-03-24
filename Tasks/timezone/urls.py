from django.urls import path
from .views import *
urlpatterns = [
    path('zone/',password.as_view()),
]



