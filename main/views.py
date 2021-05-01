from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, item
# Create your views here.

def index(response):
     return render(response, 'main/index.html', {})
 
def experiments(response):
    return render(response, 'main/experiments.html', {})
