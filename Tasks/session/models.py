from django.db import models

# Create your models here.
class person(models.Model):
    username = models.CharField(max_length=90)
    password = models.CharField(max_length=70)
    gender = models.CharField(max_length=80)

class Meta:
    db_tables = 'registration_details'