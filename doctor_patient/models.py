from django.db import models

# Create your models here.
class Doctor(models.Model):
    # Personal Detail
    name = models.CharField(max_length=70)
    dob = models.CharField(max_length=70)
    gender = models.CharField(max_length=10)
    email = models.EmailField(max_length=70)
    mobile = models.CharField(max_length=15)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=50)
    nationality = models.CharField(max_length=50)
    zipcode = models.IntegerField(max_length=10)
    bio = models.CharField(max_length=250)
    
    # Work Detail
    imcid = models.CharField(max_length=20)
    regno = models.CharField(max_length=20)
    specialization = models.CharField(max_length=50)
    shift = models.CharField(max_length=20)
    degree = models.CharField(max_length=70)
    online_profile_link = models.CharField(max_length=150)
    yoe = models.IntegerField(max_length=5)
    language = models.CharField(max_length=50)
    available = models.IntegerField(max_length=4)
    fees = models.IntegerField(max_length=10)
  
  
class Patient(models.Model):
    email = models.EmailField(max_length=70)
    userid = models.CharField(max_length=50)    
    password = models.CharField(max_length=50)    


class Admin(models.Model):
    email = models.EmailField(max_length=70)
    password = models.CharField(max_length=50)    
