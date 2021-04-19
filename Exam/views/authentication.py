from django.views.generic import TemplateView
from django.shortcuts import render,redirect


class SignUpView(TemplateView):
    template_name = 'registration/signup.html'

def home(request):
    if request.user.is_authenticated:
        if request.user.is_teacher:
            return redirect("teachers:home")
        else:
            return redirect("students:home")

    return render(request, 'home.html')

def confirm(request):
    return render(request, 'confirm.html')
    