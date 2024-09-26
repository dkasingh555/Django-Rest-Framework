from django.shortcuts import HttpResponse
from django.shortcuts import render
from .models import Carlist,Studentlist
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
# from MyApp.serializers import Carserializers
from MyApp.api_file.serializers import Carserializers
from MyApp.api_file.StuSerializers import StudentSerializers
from rest_framework import status

@api_view()
def car_list_view(request):
    car=Carlist.objects.all()
    serializer=Carserializers(car,many=True)
    return Response(serializer.data)


@api_view()
def car_details(request,pk):
    car=Carlist.objects.get(pk=pk)
    serializer=Carserializers(car)
    return Response(serializer.data)


@api_view(['GET','POST'])
def Stu_list_view(request):
    if request.method=='GET':
        student=Studentlist.objects.all()
        serializer=StudentSerializers(student,many=True)
        return Response(serializer.data)
    if request.method=='POST':
        serializer=StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

@api_view(['GET','PUT','DELETE'])
def Stu_details(request,pk):
    if request.method=='GET':
        # student=Studentlist.objects.get(pk=pk)
        try:
            student=Studentlist.objects.get(pk=pk)
        except: 
            return Response({'Error':'Student Not Found'},status=status.HTTP_404_NOT_FOUND)
        serializer=StudentSerializers(student)
        return Response(serializer.data)
    if request.method=='PUT':
        student=Studentlist.objects.get(pk=pk)
        serializer=StudentSerializers(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    if request.method=='DELETE':
        student=Studentlist.objects.get(pk=pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

 
