from django.db import models
# Create your models here.
class register(models.Model):
    fullName = models.CharField(max_length=50)
    email_id = models.EmailField(unique=True)
    Password = models.CharField(max_length=80)
    address = models.CharField(max_length=60)
    objects = models.Manager()


    class Meta:
        db_table: "react_javascript"


