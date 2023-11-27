from django.db import models

class RegisterUser(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    username = models.CharField(max_length=20,unique=True)
    emailid = models.EmailField(unique=True)
    phonenumber = models.CharField(max_length=13,unique=True)
    Password = models.CharField(max_length=80)
    objects = models.Manager()

    class Meta:
        db_table: "Register"
