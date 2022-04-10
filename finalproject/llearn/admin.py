from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','stu_id','stu_name', 'stu_email']

# admin.site.register(Student,StudentAdmin)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name','email','password']
