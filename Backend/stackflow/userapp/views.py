from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from .models import *


from django.contrib import messages


def index(request):

    return render(request, 'index.html')


def profile(request):

    return render(request, 'profile.html', {'user': request.user})


def questions(request):

    return render(request, 'questions.html')


def questionDetails(request):

    return render(request, 'questionsDetail.html')


def tags(request):

    return render(request, 'tags.html')


def users(request):

    return render(request, 'users.html')


def Login(request):
    
    error_message = None

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)  # Use Django's login function

            return redirect('questions')  # Replace with your success URL
        else:
            error_message = "Invalid username or password. Please try again."

    return render(request, 'login.html', {'error_message': error_message})

def cikis(request):
    
    logout(request)
    return redirect('home')



def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        display_name = request.POST.get('display_name')
        password = request.POST.get('password')

        if email and display_name and password:
            user = CustomUser.objects.create(
                email=email,
                display_name=display_name,
                is_active=True  # You might want to set this to True if you want users to be active upon registration
            )
            user.set_password(password)
            user.save()

            # Optionally, log in the user here

            return redirect('login')  # Replace with your success URL

    return render(request, 'register.html')
