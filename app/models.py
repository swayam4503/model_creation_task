from django.db import models

# Create your models here.
class Country(models.Model):
    c_name=models.CharField(max_length=100, primary_key=True)
class State(models.Model):
    c_name=models.ForeignKey(Country,on_delete=models.CASCADE)
    state_name=models.CharField(max_length=100)
    capital=models.CharField(max_length=100)