from django.urls import path, include
from .views import teacher, authentication


urlpatterns = [
    path('home', teacher.home, name='home'),
    path('add/course', teacher.add_course, name='add_course'),

    
    path('confirm/', authentication.confirm , name='confirm'),
]