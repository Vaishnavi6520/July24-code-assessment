from django.db import models
from patients.models import Patientsapp
from rest_framework import serializers
from django.db.models import fields

class PatientsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Patientsapp
        fields=('patient_code','name','address','disease','admitstatus')
