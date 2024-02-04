from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.

# views.py
from rest_framework import generics
from django.contrib.auth.models import User
from .models import Teacher, Student, Mark, InventoryItem
from .serializers import TeacherSerializer, StudentSerializer, MarkSerializer, InventoryItemSerializer, UserSerializer

class TeacherListCreateView(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class StudentListCreateView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class MarkListCreateView(generics.ListCreateAPIView):
    queryset = Mark.objects.all()
    serializer_class = MarkSerializer

class InventoryItemListCreateView(generics.ListCreateAPIView):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer