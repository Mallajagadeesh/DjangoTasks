from django.db import models

# Create your models here.
class patient(models.Model):
    weight = models.IntegerField()
    height = models.IntegerField()
    calculatedbmi = models.IntegerField()
    objects = models.Manager