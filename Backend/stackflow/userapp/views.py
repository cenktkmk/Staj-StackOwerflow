from django.shortcuts import render,redirect
from django.contrib.auth import login as auth_login, logout, authenticate
from .models import *

from django.contrib import messages

def index(request):
   return render(request, "index.html")  