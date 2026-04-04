from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required


# REGISTER
def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        role = request.POST.get('role', 'reader')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('register')

        user = User.objects.create_user(username=username, password=password)

        # set role
        user.profile.role = role
        user.profile.save()

        login(request, user)
        return redirect('home')

    return render(request, 'register.html')


# LOGIN
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)   # SESSION CREATED
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials")

    return render(request, 'login.html')


# LOGOUT
def logout_view(request):
    logout(request)  # SESSION DESTROYED
    return redirect('login')


# PROFILE VIEW
@login_required
def profile_view(request):
    profile = request.user.profile
    return render(request, 'profile.html', {'profile': profile})


# EDIT PROFILE
@login_required
def edit_profile(request):
    profile = request.user.profile

    if request.method == 'POST':
        profile.bio = request.POST['bio']

        if 'image' in request.FILES:
            profile.profile_image = request.FILES['image']

        profile.save()
        return redirect('profile')

    return render(request, 'edit_profile.html', {'profile': profile})