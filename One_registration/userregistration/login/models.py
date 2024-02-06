from django.db import models


# Create your models here.
class Registration(models.Model):
    firstname = models.CharField(max_length=12)
    lastname = models.CharField(max_length=25)
    Email_id = models.EmailField(unique=True)
    username = models.CharField(max_length=56, unique=True)
    phonenumber = models.CharField(max_length=40, unique=True)
    password = models.CharField(max_length=60)
    objects = models.Manager()

    class Meta:
        db_table = "Registration"
