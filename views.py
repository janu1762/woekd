from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django import form
from .models import *
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .form import RegistrationForm


def index(request):
    return render(request,'index.html')
def c1(request):
    return render(request,'c1.html')
def c2(request):
    return render(request,'c2.html')
def c3(request):
    return render(request,'c3.html')
def c4(request):
    return render(request,'c4.html')
def c5(request):
    return render(request,'c5.html')
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Create a new user account
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username, email, password)
            user.save()
            # Redirect to a success page
            return redirect('success')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})