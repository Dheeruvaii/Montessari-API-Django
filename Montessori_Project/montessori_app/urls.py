# urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('teachers/', TeacherListCreateView.as_view(), name='teacher-list-create'),
    path('students/', StudentListCreateView.as_view(), name='student-list-create'),
    path('marks/', MarkListCreateView.as_view(), name='mark-list-create'),
    path('inventory/', InventoryItemListCreateView.as_view(), name='inventory-list-create'),
]
