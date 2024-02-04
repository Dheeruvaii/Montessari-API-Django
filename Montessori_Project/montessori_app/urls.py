# urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('v1/org/', OrganizationApiView.as_view(), name='org-list'),
    path('teachers/', TeacherListCreateView.as_view(), name='teacher-list-create'),
    path('teachers/<int:pk>/', TeacherRetrieveUpdateDestroyView.as_view(), name='teacher-retrieve-update-destroy'),
    path('students/', StudentListCreateView.as_view(), name='student-list-create'),
    path('students/<int:pk>/', StudentRetrieveUpdateDestroyView.as_view(), name='student-retrieve-update-destroy'),
    path('marks/', MarkListCreateView.as_view(), name='mark-list-create'),
    path('marks/<int:pk>/', MarkRetrieveUpdateDestroyView.as_view(), name='mark-retrieve-update-destroy'),
    path('inventory-items/', InventoryItemListCreateView.as_view(), name='inventory-item-list-create'),
    path('inventory-items/<int:pk>/', InventoryItemRetrieveUpdateDestroyView.as_view(), name='inventory-item-retrieve-update-destroy'),
]
]
