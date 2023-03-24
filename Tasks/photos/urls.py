"""photos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('images.urls')),
    path('',include('covertimages.urls')),
    path('',include('session.urls')),
    path('',include('multiplesession.urls')),
    path('',include('orm.urls')),
    path('',include('many.urls')),
    path('',include('encryption.urls')),
    path('',include('log.urls')),
    path('',include('valid.urls')),
    path('',include('currency.urls')),
    path('',include('oauth.urls')),
    path('',include('date.urls')),
    path('',include('birth.urls')),
    path('',include('DOB.urls')),
    path('',include('qrrcode.urls')),
    path('',include('barcode.urls')),
    path('',include('BMI.urls')),
    path('',include('timezone.urls')),
    path('',include('forget.urls')),
    path('',include('currenttime.urls')),
    path('',include('decimalfield.urls')),
    path('',include('words.urls')),




]
