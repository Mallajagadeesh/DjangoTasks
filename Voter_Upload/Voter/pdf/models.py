from django.db import models


# Create your models here.

class Uploadimage(models.Model):
    Uploaded_Voter_Slip = models.ImageField(upload_to='uploaded_images/')
    objects = models.Manager

    class Meta:
        db_table = "folder_path"
