from django.urls import path
from .views import *
urlpatterns = [
    path('age/',postview.as_view()),

]