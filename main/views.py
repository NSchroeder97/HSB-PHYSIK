from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, item
# Create your views here.

def index(response):
     return render(response, 'main/index.html', {})
 
def experiments(response):
    return render(response, 'main/experiments.html', {})
 
def projects(response):
    return render(response, 'main/projects.html', {})

def impressum(response):
    return render(response, 'main/impressum.html', {})
	
def Labore(response):
    return render(response, 'main/Labore.html', {})

def Mitarbeiter(reponse):
    return render(reponse, 'main/Mitarbeiter.html', {})

def register(reponse):
    return render(reponse, 'main/register.html', {})
