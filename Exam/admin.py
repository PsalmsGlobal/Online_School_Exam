from django.contrib import admin
from .models import  Semester
from .import models

@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
  list_display = ( 'username', 'first_name', 'last_name', 'email', 'is_student', 'is_teacher',)
  list_filter = ('is_student', 'is_teacher')
  search_fields = [ 'username']

@admin.register(models.Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = [ 'subject_name', 'subject_code', 'deactivate']


@admin.register(models.Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = [ 'user', 'subject']
    search_fields = [ 'username']


@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    search_fields = [ 'username']

@admin.register(models.Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = [ 'course', 'subject']

admin.site.register(Semester)



