from django.db import models
from django.db.models import fields
from rest_framework import serializers
from donors.models import Donorapp1

class DonorSerializer(serializers.ModelSerializer):
    class Meta:
        model= Donorapp1
        fields = ('name','address','bloodgroup','mobile_no','username','password')

        
   
   

