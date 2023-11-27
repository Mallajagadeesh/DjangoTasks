from django.urls import path
from .views import Register2View,LoginView

urlpatterns = [
    path('users/', Register2View.as_view()),
    path('login/', LoginView.as_view())

]
