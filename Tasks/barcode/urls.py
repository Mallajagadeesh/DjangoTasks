from django.urls import path
from .views import *
urlpatterns = [
    path('code111/',datamodel.as_view()),
]
