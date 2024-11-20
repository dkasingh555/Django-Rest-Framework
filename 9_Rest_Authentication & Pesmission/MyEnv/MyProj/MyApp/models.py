from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Carlist(models.Model):
    name=models.CharField(max_length=50)
    desc=models.CharField(max_length=200)
    active=models.BooleanField(default=False)


class Studentlist(models.Model):
    Stu_Name=models.CharField(max_length=100)
    Stu_Class=models.IntegerField(max_length=10)
    Stu_Email=models.EmailField() 

    def __str__(self):
        return self.Stu_Name

class Schoollist(models.Model):
    School=models.CharField(max_length=200)
    Location=models.CharField(max_length=100)
    website=models.URLField(max_length=100)
    
    def __str__(self):
        return self.School


class Review(models.Model):
    rating=models.IntegerField(validators=[MaxValueValidator,MinValueValidator])
    comments=models.CharField(max_length=200,null=True)
    student=models.ForeignKey(Studentlist,on_delete=models.CASCADE,related_name="Reviews",null=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return "The Rating Of "+ self.student.Stu_Name +":---"+str(self.rating)
