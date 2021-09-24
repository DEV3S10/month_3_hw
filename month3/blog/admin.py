from django.contrib import admin

from .models import Student, Blog, Comment
# Register your models here.

admin.site.register(Student)
admin.site.register(Blog)
admin.site.register(Comment)
