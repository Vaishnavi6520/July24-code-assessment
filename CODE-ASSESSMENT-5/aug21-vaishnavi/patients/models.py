from django.db import models

# Create your models here.
class Patientsapp(models.Model):
    patient_code=models.IntegerField()
    name = models.CharField(max_length=20)
    address=models.CharField(max_length=100)
    disease=models.CharField(max_length=50)
    admitstatus=models.CharField(max_length=20)