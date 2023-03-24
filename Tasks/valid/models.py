from django.core.validators import RegexValidator
from django.db import models

# Create your models here.
class datamodel(models.Model):
    username = models.CharField(max_length=100)
    Password = RegexValidator(regex = r'^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\s\./0-9]*$',
                              message="password "
                                      'must be contain 8 letters and a capital letter and a special character')
    password = models.CharField(validators=[Password], max_length=60)
    gender = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    objects = models.Manager()
