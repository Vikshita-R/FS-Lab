from django.contrib import admin

from . models import Fruit, Student

from .models import Course, Student5
# Register your models here.

admin.site.register(Fruit)
admin.site.register(Student)

admin.site.register(Course)
admin.site.register(Student5)

