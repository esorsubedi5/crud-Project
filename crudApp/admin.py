from django.contrib import admin
from .models import StudentDetail  
@admin.register(StudentDetail)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'rollno', 'name', 'email']