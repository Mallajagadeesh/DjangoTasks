from django.db import models

# Create your models here.


class app(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)

    class meta:
        db_table = "REST FRAMES"


