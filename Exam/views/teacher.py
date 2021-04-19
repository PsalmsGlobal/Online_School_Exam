from django.shortcuts import render,redirect
from django.views.generic import CreateView
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from ..forms import TeacherSignUpForm, CourseForm
from ..models import User, Teacher, Student, Course, Subject
from ..views import *


class TeacherSignUpView(CreateView):
    model = User
    form_class = TeacherSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'teacher'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('confirm')

def home(request):
    return render(request, 'teachers/home.html')

@method_decorator(login_required, name='dispatch')
class teacherAddSubjectView(CreateView):
    model = Subject
    fields = '__all__'
    template_name = 'teachers/add_subj.html'
    
    def form_valid(self, form):
        semester = form.save(commit=False)
        semester.name = self.request.user
        semester.save()
        messages.success(self.request, 'You have been Created a Subject! Go ahead now on Semester Page.')
        return redirect('teachers:add_subject')
        

def add_course(request):
    if request.method=='POST':
        form=CourseForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['course'])        
            form.save()
            messages.success(request, 'Course Added successfully!')
            return redirect("teachers:add_course")

    else:
        form=CourseForm()
    context = {'form' : form}
    return render(request,'teachers/add_course.html',context)
