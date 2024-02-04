from django.shortcuts import render

"""this is my montessori project views using api views child view class"""
# views.py
from rest_framework import generics
# from django.contrib.auth.models import User
from .models import *
from .serializer import *
from rest_framework.views import APIView

class OrganizationApiView(APIView):
    def get(self,request):
        query=Organization.objects.all()
        serializer=OrganizationSerializer(query)
        return Response(serializer.data)

    def create(self,request,*args,**kwargs):
        query=Organization.objects.all()
        serializer=OrganizationSerializer(query,data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

class TeacherListCreateView(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class TeacherRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class StudentListCreateView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class MarkListCreateView(generics.ListCreateAPIView):
    queryset = Mark.objects.all()
    serializer_class = MarkSerializer

class MarkRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mark.objects.all()
    serializer_class = MarkSerializer

class InventoryItemListCreateView(generics.ListCreateAPIView):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer

class InventoryItemRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
