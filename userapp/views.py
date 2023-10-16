from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from .models import *
from .form import CreatePost


from django.contrib import messages


def index(request):

    return render(request, 'index.html')


def profile(request):

    return render(request, 'profile.html', {'user': request.user})

def questions(request):
    sorular = Post.objects.all()
    context = {}
    context["sorular"] = sorular
   
    
    return render(request, 'questions.html', context)


def questionDetails(request):

    return render(request, 'questionsDetail.html')


def tags(request):

    return render(request, 'tags.html')


def users(request):

    return render(request, 'users.html')



def createpost(request):
    context = {}
    if request.method == "POST":
        form = CreatePost(request.POST)
        if form.is_valid():
            postform = form.save(commit=False)
            postform.user = request.user
            postform.save()

            return redirect("questions")
    else:
        context["form"] = CreatePost

        return render(request, "createPost.html", context)    