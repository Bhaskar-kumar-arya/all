from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile

# Create your views here.

@login_required(login_url='signin')
def index(request):
    return render(request, 'index.html')
@login_required(login_url='signin')    
def settings (request) :
    user_profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        user_profileImage = request.FILES.get('profileImage')
        user_bio = request.POST.get('bio')
        user_location = request.POST.get('location')
        if user_profileImage:
            user_profile.profileimg = user_profileImage
        user_profile.bio = user_bio
        user_profile.location = user_location
        user_profile.save()       
        return redirect('settings') 
    return render(request,'settings.html',{'user_profile' : user_profile})

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
        user_login = auth.authenticate(username = username,password=password)
        auth.login(request,user_login)
        # create a profile for the user
        user_model = User.objects.get(username=username)
        new_profile = Profile.objects.create(user = user_model,id_user = user_model.id)
        new_profile.save()
        return redirect('settings')
    else :
        return render(request, 'signup.html')

def signin (request) :
    if request.method == 'POST' :
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username,password = password)
        if user :
            auth.login(request,user)
            return redirect('/')
        else :
            messages.error(request,'invalid credentials')
            return redirect('signin')
    else :
        return render(request,'signin.html')    



@login_required(login_url='signin')    
def logout (request) :
    auth.logout(request)
    return redirect('signin')    
