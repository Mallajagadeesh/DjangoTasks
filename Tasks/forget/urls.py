from django.urls import path
from .import views
from .views import *
urlpatterns =[
    path('get22/', contact_list),
    path('post22/', create_contact),
    path('update22/<int:id>', update_contact.as_view()),

]