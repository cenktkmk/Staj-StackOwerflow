from django.shortcuts import render,redirect
from django.contrib.auth import login as auth_login, logout, authenticate
from .models import *

from django.contrib import messages

def index(request):
    
    return render (request, 'index.html')
def profile(request):
    
    return render (request, 'profile.html')

def questions(request):
    
   return render(request, 'questions.html')

def questionDetails(request):
    
    return render(request, 'questionsDetail.html')

def tags(request):
    
    return render (request, 'tags.html')


def users(request):
    
    return render (request, 'users.html')