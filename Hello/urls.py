
from django.contrib import admin
from django.urls import path, include

from home.views import login_view, register_view, logout_view


admin.site.site_header ="DSC Admin"
admin.site.site_title ="DSC Admin Portal"
admin.site.index_title ="Welcome to Developer Students Club Login Portal"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('login/', login_view),
    path('register/', register_view),
    path('logout/', logout_view)
   
]
