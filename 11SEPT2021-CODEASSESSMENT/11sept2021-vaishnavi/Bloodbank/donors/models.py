from django.db import models

# Create your models here.
class Donorapp1(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=30)
    bloodgroup = models.CharField(max_length=20)
    mobile_no =models.BigIntegerField()
    username=models.CharField(max_length=20)
    password = models.CharField(max_length=20)