from django.db import models


class Student(models.Model):
    student_id = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=128)
    name = models.CharField(max_length=100)
    attendance_percentage = models.DecimalField(max_digits=5, decimal_places=2)

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    
