from django.contrib import admin
from .models import Student, Course, Grade, CoursePerStudent

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(CoursePerStudent)
admin.site.register(Grade)
