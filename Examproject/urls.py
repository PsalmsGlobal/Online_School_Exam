from django.contrib import admin
from django.urls import path, include
from Exam.views import authentication, student, teacher


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Exam.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', authentication.SignUpView.as_view(), name='signup'),
    path('accounts/signup/student/', student.StudentSignUpView.as_view(), name='student_signup'),
    path('accounts/signup/teacher/', teacher.TeacherSignUpView.as_view(), name='teacher_signup'),
    
]
