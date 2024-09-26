from django.db import models


class PriceList(models.Model):
    Country=models.CharField(max_length=100)
    FromCur=models.CharField(max_length=100)
    ToCur=models.CharField(max_length=100)
    Rate=models.IntegerField()
    LastUpdate=models.DateTimeField()
    Symbol=models.CharField(max_length=100)
    
  
