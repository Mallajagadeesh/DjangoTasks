from django.urls import path
from .views import *

urlpatterns = [
    path('word/', password.as_view()),
    path('en/', login.as_view()),

]
