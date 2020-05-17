from django.shortcuts import render, redirect
from datetime import datetime
from home.models import Contact , feedback 
from django.contrib import messages
from github import Github, GithubException
import requests
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login 
from django.contrib.auth.forms import UserCreationForm
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

def loginUser(request):
    if request.method=="POST":
        
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/idea")

        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')

    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")