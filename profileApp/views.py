
from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import get_object_or_404
from .models import CustomUser, Badge


from django.contrib import messages

# Create your views here.







def activity(request):
    return render(request, 'activity.html')




def cikis(request):
    
    logout(request)
    return redirect('home')

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





def users(request):

    user = CustomUser.objects.all()

    context = {
        "user" : user
    }



    return render(request, 'users.html', context)



def edit_profile(request):
    user_profile = request.user

    if request.method == 'POST':
        avatar = request.FILES.get('avatar')
        about_me = request.POST.get('about_me')
        location = request.POST.get('location')
        title = request.POST.get('title')
        github = request.POST.get('github')
        twitter = request.POST.get('twitter')
        website = request.POST.get('website')
        display_name = request.POST.get('display_name')

        if avatar:
            # Save the new avatar if a file was provided
            user_profile.avatar = avatar

        # Check if fields are empty, and if so, retain the existing data
        if not about_me:
            about_me = user_profile.about_me
        if not location:
            location = user_profile.location
        if not title:
            title = user_profile.title
        if not github:
            github = user_profile.github
        if not twitter:
            twitter = user_profile.twitter
        if not website:
            website = user_profile.website
        if not display_name:
            display_name = user_profile.display_name

        user_profile.about_me = about_me
        user_profile.location = location
        user_profile.title = title
        user_profile.github = github
        user_profile.twitter = twitter
        user_profile.website = website
        user_profile.display_name = display_name

        user_profile.save()

        return redirect('questions')
    
    return render(request, 'settings.html', {'user_profile': user_profile})


def userProfile(request, user_uuid):
    user = get_object_or_404(CustomUser, user_uuid=user_uuid)
    user_to_display = get_object_or_404(CustomUser, user_uuid=user_uuid)
    is_following = request.user.is_following(user_to_display)
    followers_count = user.followers.count()
    following_count = user.following.count()
    badges = user.badge.all()

    context = {
        'badges': badges,
        'user_to_display': user_to_display,
        'is_following': is_following,
        'user':user,
        'followers_count': followers_count,
        'following_count': following_count,
    }

    return render(request, 'profile-user.html', context)

def follow_view(request, user_uuid):
    user_to_follow = CustomUser.objects.get(user_uuid=user_uuid)
    request.user.follow(user_to_follow)
    return redirect('userProfile', user_uuid=user_uuid)  # Profil sayfasına yönlendirme yapabilirsiniz.

def unfollow_view(request, user_uuid):
    user_to_unfollow = CustomUser.objects.get(user_uuid=user_uuid)
    request.user.unfollow(user_to_unfollow)
    return redirect('userProfile', user_uuid=user_uuid)  # Profil sayfasına