from django.shortcuts import render
from .models import Carlist
from django.http import JsonResponse
# Create your views here.


def car_list_view(request):
    cars=Carlist.objects.all()
    data={
        'cars':list(cars.values()),
    }
    return JsonResponse(data)



def car_datails(request,pk):
    car=Carlist.objects.get(pk=pk)
    data={
        'name':car.name,
        'desc':car.desc,
        'active':car.active,
    }
    return JsonResponse(data)