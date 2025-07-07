from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from .models import *
from django.contrib.auth import login as auth_login,authenticate,logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def home(request):
    videos = Video.objects.order_by('-uploaded_at')
    return render(request, 'index.html',{'videos' : videos})

def upload_video(request):
    if request.method == 'POST' :
        form = VideoForm(request.POST,request.FILES)
        if form.is_valid() :
            video = form.save(commit=False)
            video.channel = request.user.channel
            video.save()
            return redirect('home')
        else :
            return render(request, 'upload.html',{'form' : form})
    else :
        form = VideoForm()
        return render(request, 'upload.html',{'form' : form})
    
def signup (request) :
    if request.method == 'POST': 
        form = RegisterForm(request.POST) 
        if form.is_valid():
            print("valid signup")
            user = form.save()
            channel = Channel.objects.create(user=user, name=form.cleaned_data['channel_name'])
            channel.save()
            auth_login(request, user)
            return redirect('home')
        else:
            print(f"invalid form registration {form.errors}")
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})

def login(request) :
    if request.method == 'POST' :
        form = AuthenticationForm(request,data = request.POST) 
        if form.is_valid() :
            user = form.get_user() 
            auth_login(request,user)
            return redirect(request,'home.html')
    else :
        form = AuthenticationForm()
    return render(request,'login.html',{'form' : form})     