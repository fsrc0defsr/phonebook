from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'home.html')

login_view = LoginView.as_view(template_name='login.html')

@login_required
def profile(request):
    return render(request, 'profile.html')

def logout_view(request):
    LogoutView.as_view()(request)
    return redirect('login')