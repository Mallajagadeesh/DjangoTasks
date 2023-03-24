from django.db import models

# Create your models here.
class decimal(models.Model):
    number = models.FloatField()
    digits = models.IntegerField()
    decimalvalue = models.CharField(max_length=200)
    objects = models.Manager