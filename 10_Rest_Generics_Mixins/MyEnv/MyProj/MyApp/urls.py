from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('student/', views.Stu_list_view, name='student'),
    path('student/<int:pk>/', views.Stu_details, name='Stu_details'),
    path('school/', views.School.as_view(), name='School'),
    path('school/<int:pk>/', views.School_Details.as_view(), name='Student_details'),
    path('review',views.Reviewlist.as_view(), name='Reviewlist'),
    path('review/<int:pk>/',views.Review_Details.as_view(), name='Review_Details'),
    
]
