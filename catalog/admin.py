from django.contrib import admin

# Register your models here.
from .models import Student, Teacher, Location



admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Location)