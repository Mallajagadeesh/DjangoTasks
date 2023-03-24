from django.db import models

# Create your models here.
class covert(models.Model):
    Name = models.CharField(max_length=90)
    images = models.CharField(max_length=770)

    objects=models.Manager