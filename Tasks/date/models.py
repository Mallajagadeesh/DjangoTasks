from django.db import models

# Create your models here.
class date(models.Model):
    date1 = models.DateField()
    date2 = models.DateField()
    objects = models.Manager
