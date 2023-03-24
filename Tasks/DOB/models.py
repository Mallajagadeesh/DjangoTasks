from django.db import models

# Create your models here.
class birth(models.Model):
    age = models.IntegerField()
    objects = models.Manager

