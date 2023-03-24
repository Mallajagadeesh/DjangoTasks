from django.urls import path
from .views import *
urlpatterns = [
    path('word1/',password.as_view()),
]
