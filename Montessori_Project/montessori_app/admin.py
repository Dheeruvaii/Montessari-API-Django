# from django.contrib import admin

# # Register your models here.
# from .models import *

# admin.site.register(Organization)
# admin.site.register(Teacher)
# admin.site.register(Student)
# admin.site.register(Mark)
# admin.site.register(InventoryItem)


from django.contrib import admin
from .models import Organization, Teacher, Student, Mark, InventoryItem

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('org_name', 'organization_category', 'created_at', 'updated_at')

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('username', 'subject', 'Permanent_address', 'temporary_address')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('username', 'grade', 'father_name', 'Mother_name', 'Permanent_address', 'temporary_address')

@admin.register(Mark)
class MarkAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject', 'score', 'checked_by')

@admin.register(InventoryItem)
class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'item_code', 'quantity', 'category', 'created_by', 'description', 'expiry_reminder', 'low_stock_reminder', 'updated_at', 'purchase_date', 'expiry_date')
