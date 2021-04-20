from django.views.generic import TemplateView
from django.shortcuts import render,redirect
from django.conf import settings
from django.contrib.auth.forms import  UserChangeForm


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

def edit_profile(request):
	if request.method == 'POST':
		form = EditProfileForm(request.POST, instance= request.user)
		if form.is_valid():
			form.save()
			messages.success(request,('You Have Edited Your Profile...'))
			return redirect('home')
	else:
		form = EditProfileForm(instance= request.user)

	context = {'form': form}
	return render(request, 'registration/edit_profile.html', context)
    