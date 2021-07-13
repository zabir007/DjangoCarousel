from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.

class Slider(models.Model):
    thumbnail = CloudinaryField(folder="carousel/")
    tittle = models.TextField()
    descp = models.TextField()

class Feature(models.Model):
    thumbnail = CloudinaryField(folder="carousel/")
    tittle = models.TextField()
    descp = models.TextField()


class Another(models.Model):
    imagefield = CloudinaryField(folder="carousel/")
    tittle = models.TextField()
    descp = models.TextField()



