from django.db import models
from doctors.models import Doctorsapp
from rest_framework import serializers
from django.db.models import fields

class DoctorsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Doctorsapp
        fields=('doctor_code','name','address','speciality','username','password')
