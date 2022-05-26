from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin


@admin.register(Student)
class StudentAdmin(ImportExportModelAdmin):
    list_display = ['id', 'teacher_name', 'name', 'email', 'age', 'roll', 'address']


@admin.register(Teacher)
class StudentAdmin(ImportExportModelAdmin):
    list_display = ['id', 'name', 'subject', 'age']

