from django.views.generic import CreateView
from django.shortcuts import get_object_or_404, redirect, render
from ..forms import StudentSignUpForm
from ..models import User, Student


class StudentSignUpView(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        request = self.request
        if request.method == 'POST':
            email = request.POST.get('email')
            if User.objects.filter(email = email).first():
                messages.success(request, 'Email is taken.')
                return redirect('student_signup')
            user = form.save()
        return render(request , 'registration/signup_form.html')