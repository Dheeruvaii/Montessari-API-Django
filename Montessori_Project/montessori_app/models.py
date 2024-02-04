"""this is my montessori project models"""
from django.db import models


class Teacher(models.Model):
    username=models.CharField(max_length=20)
    subject = models.CharField(max_length=50)

class Student(models.Model):
    username=models.CharField(max_length=20)
    grade = models.CharField(max_length=10)

class Mark(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)
    score = models.DecimalField(max_digits=5, decimal_places=2)

class InventoryItem(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    description = models.TextField()