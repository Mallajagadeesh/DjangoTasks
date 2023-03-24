from django.urls import path
from .views import *
urlpatterns = [
    path('birth1/',password.as_view()),
]
