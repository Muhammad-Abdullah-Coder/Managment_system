from django.contrib import admin
from .models import Student

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'occupation', 'present_percentage', 'good_work_percentage', 'joining_month', 'joining_year')
    search_fields = ('name', 'occupation')