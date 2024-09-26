from django.urls import path
from . import views

urlpatterns = [
    path('', views.displaydata, name='Displaydata'),
    path('currency/', views.Currency_list, name='Currency'),
    
    # path('car/<int:pk>/', views.car_details, name='Car_details'),
    # path('student/', views.Stu_list_view, name='student'),
    # path('student/<int:pk>/', views.Stu_details, name='Stu_details'),
    
]
