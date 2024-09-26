from django.urls import path
from . import views

urlpatterns = [
    # path('car/', views.car_list_view, name='car'),
    # path('car/<int:pk>/', views.car_details, name='Car_details'),
    path('student/', views.Stu_list_view, name='student'),
    path('student/<int:pk>/', views.Stu_details, name='Stu_details'),
    
]
