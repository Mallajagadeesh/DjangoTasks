from django.db import models

# Create your models here.
class times(models.Model):
    username = models.CharField(max_length=500)
    email = models.CharField(max_length=50)
    time = models.CharField(max_length=200)
    objects = models.Manager