from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=200)
    age=models.IntegerField()
    email=models.EmailField(unique=True)
    phone=models.BigIntegerField()

    
    class Meta:
        db_table="student_tb"