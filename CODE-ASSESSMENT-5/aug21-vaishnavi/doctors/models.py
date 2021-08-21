from django.db import models

# Create your models here.
class Doctorsapp(models.Model):
    doctor_code=models.IntegerField()
    name = models.CharField(max_length=20)
    address=models.CharField(max_length=100)
    speciality=models.CharField(max_length=50)
    username=models.CharField(max_length=10)
    password=models.CharField(max_length=10)