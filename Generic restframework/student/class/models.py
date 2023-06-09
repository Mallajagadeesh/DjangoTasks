from django.db import models


# Create your models here.
class app(models.Model):
    institute = models.CharField(max_length=70)
    address = models.CharField(max_length=60)


class branchmodel(models.Model):
    subject = models.ForeignKey(app,on_delete=models.CASCADE)
    branch = models.CharField(max_length=25)
    objects = models.Manager

    class Meta:
        db_table: "branchtable"


