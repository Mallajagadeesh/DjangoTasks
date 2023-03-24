from django.db import models
# Create your models here.
class qrcode(models.Model):
    product_namer = models.CharField(max_length=500)
    product_code = models.CharField(max_length=50)
    pack_code = models.CharField(max_length=400)
    qr_code = models.BinaryField(max_length=600)
    objects = models.Manager

