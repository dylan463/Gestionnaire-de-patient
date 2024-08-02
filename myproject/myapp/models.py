from django.db import models
from datetime import datetime

# Create your models here.
class patient(models.Model):
    name= models.CharField(max_length =100)
    job= models.CharField(max_length =100)
    contact = models.CharField(max_length = 14,default = "")

class consultation(models.Model):
    date = models.DateTimeField(default = datetime.now,blank = True)
    idpatient = models.ForeignKey(patient,on_delete=models.CASCADE)
    description = models.CharField(max_length = 10000)
