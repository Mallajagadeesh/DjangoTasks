from django.urls import path
from .views import *

urlpatterns = [
    path('object/',postview.as_view()),
    path('get1/', getview.as_view()),
]
