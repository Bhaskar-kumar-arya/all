from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Profile

# Create your views here.
def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')   
        password2 = request.POST.get('password2') 
        email = request.POST.get('email')
        print(username, password, email)

        if password != password2:
            messages.error(request, "Passwords do not match!")
            return redirect('signup')
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists!")
            return redirect('signup')
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('signup')
        user = User.objects.create_user(username=username,password=password,email=email)
        user.save()
        # create a profile for the user
        user_model = User.objects.get(username=username)
        new_profile = Profile.objects.create(user = user_model,id_user = user_model.id)
        new_profile.save()
        return redirect('signup')
    else :
        return render(request, 'signup.html')
