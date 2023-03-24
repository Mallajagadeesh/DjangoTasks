from django.db import models
from io import BytesIO
from django.core.files import File
from PIL import Image,ImageDraw
# Create your models here.
class barcode(models.Model):
    product_name = models.CharField(max_length=500)
    product_code = models.CharField(max_length=50)
    pack_code = models.CharField(max_length=400)
    br_code = models.BinaryField(max_length=600)
    objects = models.Manager
