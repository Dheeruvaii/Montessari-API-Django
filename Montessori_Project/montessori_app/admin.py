from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Organization)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Mark)
admin.site.register(InventoryItem)

