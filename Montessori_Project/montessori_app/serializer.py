# serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Teacher, Student, Mark, InventoryItem

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class TeacherSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Teacher
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Student
        fields = '__all__'

class MarkSerializer(serializers.ModelSerializer):
    student = UserSerializer()

    class Meta:
        model = Mark
        fields = '__all__'

class InventoryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryItem
        fields = '__all__'
