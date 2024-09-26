from django.shortcuts import HttpResponse
from django.shortcuts import render
# from .models import Carlist,Studentlist
from .models import PriceList
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
# from MyApp.serializers import Carserializers
from MyApp.api_file.Currencyserializers import Currencyserializers
from rest_framework import status
from django.shortcuts import render
import requests

# @api_view()
# def car_details(request):
#     car=Carlist.objects.all()
#     serializer=Carserializers(Result,many=True)
#     return Response(serializer.data)


# @api_view()
# def car_details(request,pk):
#     car=Carlist.objects.get(pk=pk)
#     serializer=Carserializers(car)
#     return Response(serializer.data)


# @api_view(['GET','POST'])
# def Stu_list_view(request):
#     if request.method=='GET':
#         student=Studentlist.objects.all()
#         serializer=StudentSerializers(student,many=True)
#         return Response(serializer.data)
#     if request.method=='POST':
#         serializer=StudentSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)

# @api_view(['GET','PUT','DELETE'])
# def Stu_details(request,pk):
#     if request.method=='GET':
#         # student=Studentlist.objects.get(pk=pk)
#         try:
#             student=Studentlist.objects.get(pk=pk)
#         except: 
#             return Response({'Error':'Student Not Found'},status=status.HTTP_404_NOT_FOUND)
#         serializer=StudentSerializers(student)
#         return Response(serializer.data)
#     if request.method=='PUT':
#         student=Studentlist.objects.get(pk=pk)
#         serializer=StudentSerializers(student,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#     if request.method=='DELETE':
#         student=Studentlist.objects.get(pk=pk)
#         student.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

@api_view()
def Currency_list(request):
    Result=PriceList.objects.all()
    serializer=Currencyserializers(Result,many=True)
    return Response(serializer.data) 

def displaydata(request):
    callapi=requests.get('http://127.0.0.1:8000/currency/')
    
    if callapi.status_code == 200:
        result = callapi.json()
        return render(request, 'exchange_rate.html', {'PriceList': result})
    else:
        error_message = "Failed to fetch data from the API."
        return render(request, 'error.html', {'error_message': error_message})