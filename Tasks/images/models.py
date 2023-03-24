from django.db import models

# Create your models here.
class images(models.Model):
    Name = models.CharField(max_length=80)
    images = models.ImageField()
    data = models.DateTimeField(auto_now=True)
    objects = models.Manager