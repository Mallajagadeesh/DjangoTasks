from django.contrib.auth import logout
from django.urls import path
from .views import *
urlpatterns = [
    path('token/',file.as_view()),
    path('login1/', loginview.as_view()),

]
