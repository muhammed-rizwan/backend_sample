from django.urls import path
from . import views
from .views import StudentListCreate,StudentRetrieveUpdateDistroy,FirstFiveStudent


urlpatterns=[
    path('students/',StudentListCreate.as_view(),name='student-ListCreate'),
    path('student/<int:pk>',StudentRetrieveUpdateDistroy.as_view(),name='student-detail'),
    path('student/first5/',FirstFiveStudent.as_view(),name='first-five-students'),
]