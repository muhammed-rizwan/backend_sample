from django.shortcuts import render
from rest_framework import generics
from .models import Student
from .serializers import StudentSerializer
# Create your views here.


class StudentListCreate(generics.ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer


class StudentRetrieveUpdateDistroy(generics.RetrieveUpdateDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class FirstFiveStudent(generics.ListAPIView):
    queryset=Student.objects.all()[:5]
    serializer_class=StudentSerializer

