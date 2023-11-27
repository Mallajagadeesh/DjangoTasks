from django.db import models

class User(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    username = models.CharField(max_length=20,unique=True)
    emailid = models.EmailField(unique=True)
    phonenumber = models.CharField(max_length=13,unique=True)
    constituency = models.CharField(max_length=100)
    Password = models.CharField(max_length=80)
    mandal = models.CharField(max_length=100)
    pollingstation = models.CharField(max_length=100)
    pollingstationnumber = models.CharField(max_length=100)

    objects = models.Manager()

    class Meta:
        db_table: "deatils"
