from django.db import models


# class Carlist(models.Model):
#     name=models.CharField(max_length=50)
#     desc=models.CharField(max_length=200)
#     active=models.BooleanField(default=False)


class Studentlist(models.Model):
    Stu_Name=models.CharField(max_length=100)
    Stu_Class=models.IntegerField(max_length=10)
    Stu_Email=models.EmailField()

