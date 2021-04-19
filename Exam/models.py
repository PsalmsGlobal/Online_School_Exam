from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

class Subject(models.Model):
    subject_name = models.CharField(max_length=30)
    subject_code = models.IntegerField()
    deactivate = models.BooleanField(default=False)

    def __str__(self):
        return self.subject_name

class Semester(models.Model):
    semester_name = models.CharField(max_length=30)
    subject = models.ManyToManyField(Subject, related_name='+')

    def __str__(self):
        return self.semester_name

class Course(models.Model):
    course = models.CharField(max_length=30)
    color = models.CharField(max_length=7, default='#007bff')
    semester = models.ManyToManyField(Semester, related_name='+')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.course

    def get_html_badge(self):
        course = escape(self.course)
        color = escape(self.color)
        html = '<span class="badge badge-primary" style="background-color: %s">%s</span>' % (color, course)
        return mark_safe(html)


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
 
