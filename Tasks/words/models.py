from django.db import models

# Create your models here.
class words(models.Model):
    currency = models.IntegerField()
    covert = models.CharField(max_length=400)
    objects = models.Manager