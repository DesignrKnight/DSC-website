from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index,name='home'),
    path("events",views.events,name='events'),
    path("project",views.project,name='project'),
    path("team",views.team,name='team'),
    path("idea",views.idea,name='idea'),
    path('login',views.loginUser, name="login"),
    path('logout',views.logoutUser, name="logout"),
    
]
