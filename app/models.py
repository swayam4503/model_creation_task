from django.db import models

# Create your models here.
class Country(models.Model):
    c_name=models.CharField(max_length=100, primary_key=True)
class Capital(models.Model):
    c_name=models.ForeignKey(Country,on_delete=models.CASCADE)
    capital_name=models.CharField(max_length=100)