from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact , feedback
from django.contrib import messages
from github import Github, GithubException
import requests
 #Create your views here.
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
    search_result = {}
    if 'username' in request.GET:
        username = request.GET['Praisysam']
        client = Github('Praisysam', 'Praisy4822')

        try:
            user = client.get_user(username)
            search_result['name'] = user.name
            search_result['login'] = user.login
            search_result['public_repos'] = user.public_repos
            search_result['success'] = True
        except GithubException as ge:
            search_result['message'] = ge.data['message']
            search_result['success'] = False

        rate_limit = client.get_rate_limit()
        search_result['rate'] = {
            'limit': rate_limit.rate.limit,
            'remaining': rate_limit.rate.remaining,
        }

    return render(request, 'events.html', {'search_result': search_result})
    #return render(request,'events.html')

def idea(request):
    if request.method == "POST" :
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        
        idea = Contact(name=name , email=email , desc= desc , date= datetime.today() )
        idea.save()
        messages.success(request,'Your form has been sent!')
    return render (request,'idea.html')