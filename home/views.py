from django.shortcuts import render, redirect
from datetime import datetime
from home.models import Contact , feedback 
from django.contrib import messages
from github import Github, GithubException
import requests
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login 
from django.contrib.auth.forms import UserCreationForm


from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)

from .forms import UserLoginForm, UserRegisterForm

 #Create your views here.

 #password for test user is simmi2428
def index(request):
    if request.method == "POST" :
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        
        index = feedback(name=name , desc= desc , date= datetime.today() )
        index.save()
        messages.success(request,'Your feedback form has been sent!')
    return render(request,'index.html')
    #return HttpResponse("this is homepage")

def project(request):
    return render(request,'project.html')

def team(request):
    return render(request,'team.html')

def events(request):
    return render(request, 'events.html')
    #return render(request,'events.html')

def idea(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect("/login") 
    if request.method == "POST" :
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        
        idea = Contact(name=name , email=email , desc= desc , date= datetime.today() )
        idea.save()
        messages.success(request,'Your form has been sent!')
    return render (request,'idea.html')



def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('/idea')

    context = {
        'form': form,
    }
    return render(request, "login.html", context)


def register_view(request):
    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect('/idea')

    context = {
        'form': form,
    }
    return render(request, "signup.html", context)


def logout_view(request):
    logout(request)
    return redirect('/idea')
