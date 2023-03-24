from django.urls import path
from .views import *

urlpatterns = [
    path('object1/',postview.as_view()),
    path('get3/', getview.as_view()),
]
