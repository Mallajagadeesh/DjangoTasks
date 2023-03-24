from django.db import models

# Create your models here.

class details(models.Model):
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=52)
    contact= models.CharField(max_length=52)

    def __str__(self):
        return "%s the details" % self.username


class page(models.Model):
    place=models.OneToOneField(details,on_delete=models.CASCADE,primary_key=True)
    # details_name=models.CharField(max_length=800)
    # details_cat=models.CharField(max_length=400)
    # details_publish_date=models.DateField()
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

    def __str__(self):
        return "%s the restaurant" % self.place.name
#
# class information(models.Model):
#     subject = models.ForeignKey(details, on_delete=models.CASCADE)
#     name = models.CharField(max_length=65)
#
#     def __str__(self):
#         return self.subject, self.name












