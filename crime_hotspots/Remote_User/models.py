from django.db import models

# Create your models here.
from django.db.models import CASCADE


class ClientRegister_Model(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=10)
    phoneno = models.CharField(max_length=10)
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)

class crime_hotspots_model(models.Model):


    City = models.CharField(max_length=300)
    names = models.CharField(max_length=300)  # AREA NAME
    population = models.CharField(max_length=300)
    Hotspot_Name = models.CharField(max_length=300)
    Street_name = models.CharField(max_length=300)
    Address = models.CharField(max_length=300)
    Crime_Type = models.CharField(max_length=300)
    Number_Of_Crimes = models.IntegerField()
    Crime_Evidence = models.CharField(max_length=300)
    Action_Taken = models.CharField(max_length=300)
    Crime_DateTime = models.CharField(max_length=300)


class review_Model(models.Model):
    uname = models.CharField(max_length=100)
    ureview = models.CharField(max_length=100)
    sanalysis = models.CharField(max_length=100)
    dt= models.CharField(max_length=300)
    tname= models.CharField(max_length=300)
    feedback = models.CharField(max_length=300)

class recommend_Model(models.Model):
    uname1 = models.CharField(max_length=100)
    pname = models.CharField(max_length=100)
    loc = models.CharField(max_length=100)
    dt= models.CharField(max_length=300)
    usefull= models.CharField(max_length=300)

class crime_ratio_model(models.Model):
      names = models.CharField(max_length=300)
      ratio = models.CharField(max_length=300)

class search_ratio_model(models.Model):
    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)



