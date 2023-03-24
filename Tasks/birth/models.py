from django.db import models

# Create your models here.
class birth(models.Model):
    dob = models.DateField()
    age = models.IntegerField()
    objects = models.Manager

