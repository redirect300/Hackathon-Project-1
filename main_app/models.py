from django.db import models

# Create your models here.

class Hospital(models.Model):
    name = models.CharField(max_length=100)
    ucord1 = models.CharField(max_length=100)
    ucord2 = models.CharField(max_length=100)
    total_beds = models.IntegerField()
    free_beds = models.IntegerField()

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    phone = models.IntegerField()
    speciality = models.CharField(max_length=100)