from django.db import models

# Create your models here.
class manpower(models.Model):
    uname = models.CharField(max_length=20)
    email= models.CharField(max_length=50)
    phone= models.CharField(max_length=20)
    age = models.CharField(max_length=10)    