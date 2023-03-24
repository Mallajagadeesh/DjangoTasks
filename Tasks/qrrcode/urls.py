from django.urls import path
from .views import datamodel
urlpatterns = [
    path('qrcode/',datamodel.as_view()),

]
