from django.db import models

# Create your models here.
class details(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    gender = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    objects = models.Manager()
