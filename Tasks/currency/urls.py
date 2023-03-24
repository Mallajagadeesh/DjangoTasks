from django.urls import path
from .views import *
urlpatterns = [
     path('money/',Reg.as_view())
]