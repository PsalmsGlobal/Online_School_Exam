from django.urls import path, include
from .views import teacher, authentication


urlpatterns = [

    path('confirm/', authentication.confirm , name='confirm'),
    path('edit_profile/',authentication.edit_profile, name="edit_profile"),


    path('teacher/', include(([
    path('', teacher.home, name='home'),
    path('add/course', teacher.AddCourseView.as_view(), name='add_course'),
    path('add/semester', teacher.AddSemesterView.as_view(), name='add_semester'),
    #path('subjects/', teacher.AssignSubjectView.as_view(), name='choose_subject'),
    path('add/subject', teacher.AddSubjectView.as_view(), name='add_subject'),
    path('choose/subject/', teacher.ChooseSubjectView.as_view(), name='choose_subject'),
    ],  'authentication'), namespace='teachers')),
    
   
]