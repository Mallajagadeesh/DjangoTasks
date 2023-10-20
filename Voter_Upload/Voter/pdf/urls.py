from django.urls import path
from .views import *

urlpatterns = [
    path('uploadimage/', Uploadimage.as_view()),

]