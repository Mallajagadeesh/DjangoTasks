from django.db import models
# Create your models here
class Logging(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=200)
    gender = models.CharField(max_length=500)
    objects = models.Manager

