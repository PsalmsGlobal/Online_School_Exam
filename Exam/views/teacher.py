from django.shortcuts import render,redirect
from django.views.generic import CreateView, ListView, UpdateView
from django.contrib.auth import login
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from ..forms import TeacherSignUpForm, SubjectForm, CourseForm
from ..models import User, Teacher, Student, Course, Subject, Semester
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
    return render(request,'teachers/home.html')


@method_decorator(login_required, name='dispatch')
class AddSubjectView(CreateView):
    model = Subject
    fields =('subject_name', 'subject_code' )
    template_name = 'teachers/add_subject.html'
    
    def form_valid(self, form):
        semester = form.save(commit=False)
        semester.name = self.request.user
        semester.save()
        messages.success(self.request, 'You have been Created a Subject! Go ahead now on Semester Page.')
        return redirect('teachers:add_semester')

@method_decorator(login_required, name='dispatch')
class AddSemesterView(CreateView):
    model = Semester
    fields = '__all__'
    template_name = 'teachers/add_semester.html'
    
    def form_valid(self, form):
        course = form.save(commit=False)
        course.name = self.request.user
        course.save()
        messages.success(self.request, 'You have been Added a Sem! Go ahead now on Course Page.')
        return redirect('teachers:add_course')


@method_decorator([login_required], name='dispatch')
class ChooseSubjectView(CreateView):
    model = Course
    fields = ('subject', )
    template_name = 'teachers/choose_subject.html'

    def form_valid(self, form):
        subject = form.save(commit=False)
        subject = self.request.user
        subject.save()
        messages.success(self.request, 'aadsd')
        return redirect('teachers:choose_subject')

@method_decorator(login_required, name='dispatch')
class AddCourseView(CreateView):
    model = Course
    fields = ('course', 'subject')
    template_name = 'teachers/add_course.html'
    
    def form_valid(self, form):
        course = form.save(commit=False)
        course.name = self.request.user
        course.save()
        messages.success(self.request, 'You have been Added a Sem! Go ahead now on Course Page.')
        return redirect('teachers:add_course')

# @method_decorator([login_required], name='dispatch')
# class AssignSubjectView(UpdateView):
#     model = Teacher
#     form_class = SubjectForm
#     template_name = 'teachers/choose_subject.html'
#     success_url = reverse_lazy('teachers:home')

#     def get_object(self):
#         return self.request.user.teacher

#     def form_valid(self, form):
#         messages.success(self.request, 'Subject updated successfully!')
#         return super().form_valid(form)

