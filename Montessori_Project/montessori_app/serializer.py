# serializers.py
from rest_framework import serializers
from .models import Teacher, Student, Mark, InventoryItem


class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'

class MarkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mark
        fields = '__all__'

class InventoryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryItem
        fields = '__all__'
