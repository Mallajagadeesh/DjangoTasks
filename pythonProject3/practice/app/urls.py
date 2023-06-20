from django.urls import path
from .views import *

urlpatterns = [
    path('get/', contact_list),
    path('get details/<int:id>', getdetails),
    path('post/', post_app),
    path('update/<int:id>', update),
    path('delete/<int:id>', delete),
]
