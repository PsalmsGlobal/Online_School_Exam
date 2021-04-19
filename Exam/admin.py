from django.contrib import admin
from .models import  Semester, Course, Teacher
from .import models

@admin.register(models.Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = [ 'subject_name', 'subject_code', 'deactivate']

@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
  list_display = ( 'username', 'first_name', 'last_name', 'email', 'is_student', 'is_teacher',)
  list_filter = ('is_student', 'is_teacher')
  search_fields = [ 'username']


@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    search_fields = [ 'username']


admin.site.register(Semester)
admin.site.register(Course)
admin.site.register(Teacher)

