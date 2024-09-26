from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
# def index(request):
#     return render(request, "index.html", {})


# def index(request):
#      return HttpResponse("Hello")


@api_view()
def index(request):
    return Response({"message": "Hello, world!"})

@api_view()
def about(request):
    return Response({"message": "Hello, Akash!"})


@api_view(['GET', 'POST'])
def contact(request):
    if request.method == 'POST':
        return Response({"message": "Got some data!", "data": request.data})
    return Response({"message": "Hello, world!"})