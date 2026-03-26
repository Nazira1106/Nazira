from django.db import models

# Create your models here.
class Byujeteriya(models.Model):
    Brand = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    photo = models.ImageField(upload_to='Suwretleri/')
