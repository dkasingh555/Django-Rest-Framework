from django.db import models

class Carlist(models.Model):
    name=models.CharField(max_length=50)
    desc=models.CharField(max_length=200)
    active=models.BooleanField(default=False)