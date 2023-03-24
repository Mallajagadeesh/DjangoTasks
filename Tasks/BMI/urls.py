from django.urls import path
from .views import *
urlpatterns = [
    path('bmi/',password.as_view()),
]