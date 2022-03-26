from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
from django.urls import resolve


# Create your views here.
def home(request):
    current_url = resolve(request.path_info).url_name
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects':projects, 'current_url':current_url})
