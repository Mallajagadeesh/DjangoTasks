from django.urls import path
from .views import *

urlpatterns = [
    path('Registration/', Registration.as_view()),
    path('Login/', Login.as_view()),
]
