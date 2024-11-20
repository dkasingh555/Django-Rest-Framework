from django.shortcuts import HttpResponse
from django.shortcuts import render
from .models import Carlist,Studentlist,Schoollist
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from MyApp.api_file.serializers import Carserializers
from MyApp.api_file.StuSerializers import StudentSerializers
from MyApp.api_file.SchoolSerializers import SchoolSerializers
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser


# def index(respone):
#     return HttpResponse("<h1>Welcome To Django Rest FrameWork<h1/>")

def index(response):
    content = """
    <div style="display: flex; justify-content: center; align-items: center; height: 100vh;">
        <h1>Welcome To Django Rest FrameWork</h1>
    </div>
    """
    return HttpResponse(content)



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

class School(APIView):
    # authentication_classes=[BasicAuthentication]
    # permission_classes=[IsAuthenticated]
    # permission_classes=[AllowAny]
    # permission_classes=[IsAdminUser]

    # authentication_classes=[SessionAuthentication]
    # permission_classes=[IsAuthenticated]
    # permission_classes=[IsAdminUser]

    def get(self,request): 
        school=Schoollist.objects.all()
        serializer=SchoolSerializers(school,many=True)
        return Response(serializer.data)
    def put(self,request):
        serializer=SchoolSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class School_Details(APIView):
    def get(self,request,pk):
        try:
            school=Schoollist.objects.get(pk=pk)
        except:
            return Response({'Error':'School Not Found'},status=status.HTTP_404_NOT_FOUND)
        serializer=SchoolSerializers(school)
        return Response(serializer.data) 
    def put(self,request,pk):
        school=Schoollist.objects.get(pk=pk)
        serializer=SchoolSerializers(school,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        school=Schoollist.objects.get(pk=pk)
        school.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


    

    
        
