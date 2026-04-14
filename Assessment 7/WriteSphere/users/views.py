from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import * 
from blog.models import *
from interactions.models import *
from django.contrib.auth.models import User
from django.shortcuts import *

def profile_view(request, user_id):
    user_profile = get_object_or_404(User, id=user_id)

    posts = Post.objects.filter(author=user_profile)
    followers = Follow.objects.filter(following=user_profile).count()
    following = Follow.objects.filter(follower=user_profile).count()

    is_following = False
    if request.user.is_authenticated:
        is_following = Follow.objects.filter(
            follower=request.user,
            following=user_profile
        ).exists()


# REGISTER
def register_view(request):
    form = RegisterForm(request.POST or None)

    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('blog_list')

    return render(request, 'users/register.html', {'form': form})


#  LOGIN
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('blog_list')

    return render(request, 'users/login.html')


# LOGOUT
def logout_view(request):
    logout(request)
    return redirect('login')