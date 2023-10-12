from django.shortcuts import render,redirect
from django.contrib.auth import login as auth_login, logout, authenticate
from .models import *
from .form import *


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

def login(request):
    if request.method == "POST":
        username = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, username = username , password = password)
        if user:
            auth_login(request, user)

            return redirect("home")
    
    return render (request, 'login.html')

def log_out(request):
    logout(request)
    return redirect("home")

def register(request):
    context = {}
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = UserModel.objects.create(
            username = username,
            email = email,
            password = password
        )
        user.set_password(password)
        user.save()

        return redirect('login')
    else:
        context["form"] = RegisterForm
        return render (request, 'register.html', context)