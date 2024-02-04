"""this is my montessori project models"""
from django.db import models


class Organization(models.Model):
    org_name=models.CharField(max_length=50,unique=True)
    organization_category = models.CharField(max_length=200, unique=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.org_name


class Teacher(models.Model):
    username=models.CharField(max_length=20)
    subject = models.CharField(max_length=50)
    Permanent_address=models.CharField(max_length=20)
    temporary_address=models.CharField(max_length=20)

    def __str__(self):
        return self.subject


class Student(models.Model):
    username=models.CharField(max_length=20)
    grade = models.CharField(max_length=10)
    father_name=models.CharField(max_length=20)
    Mother_name=models.CharField(max_length=20)
    Permanent_address=models.CharField(max_length=20)
    temporary_address=models.CharField(max_length=20)

    def __str__(self):
        return self.username



class Mark(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)
    score = models.DecimalField(max_digits=5, decimal_places=2)
    checked_by=models.ForeignKey(Teacher,on_delete=models.CASCADE)

    def __str__(self):
        return self.student


class InventoryItem(models.Model):
    item_name = models.CharField(max_length=100)
    item_code = models.CharField(max_length=10)
    quantity = models.PositiveIntegerField()
    category = models.CharField(max_length=50)
    created_by = models.ForeignKey(Organization, on_delete=models.CASCADE)
    description = models.TextField()
    expiry_reminder = models.CharField(max_length=50, null=True, blank=True)
    low_stock_reminder = models.CharField(max_length=50, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    # created_at = models.DateTimeField(auto_now=True)
    purchase_date = models.DateField()
    expiry_date = models.DateField()
    
    def __str__(self):
        return self.item_name