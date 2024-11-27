from django.contrib import admin
from .models import Carlist,Studentlist,Schoollist,Review


# Register your models here.
admin.site.register(Carlist)
admin.site.register(Studentlist)
admin.site.register(Schoollist)
admin.site.register(Review)