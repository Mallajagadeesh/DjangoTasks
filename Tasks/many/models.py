from django.db import models

# Create your models here.
class many(models.Model):
    username = models.CharField(max_length=80,primary_key=True)
    password = models.CharField(max_length=52)
    contact= models.CharField(max_length=52)

    def __str__(self):
        return "%s the details" % self.username


class information(models.Model):
    title = models.CharField(max_length=80)
    many = models.ForeignKey(many, on_delete=models.CASCADE)
    name = models.CharField(max_length=65)

