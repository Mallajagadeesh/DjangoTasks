import details as details
from django.urls import path
from .views import *

urlpatterns = [
    path('api', create.as_view()),
    path('view/', details.as_view()),
    path('update/<int:pk>', Friendsupdate.as_view()),
    path('delete/<int:pk>', Friendsdelete.as_view()),
    path('postcall/', dommypost.as_view()),
]
