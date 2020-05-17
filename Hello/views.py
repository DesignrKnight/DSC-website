from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def idea(request):
    return render(request, "idea.html", {})
