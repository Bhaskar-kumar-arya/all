from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,JsonResponse
from .forms import *
from .models import *
from django.contrib.auth import login as auth_login,authenticate,logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login.html')
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
            render(request, 'index.html',{'videos' : Video.objects.all()})
        else :
            print(form.errors)
    else :
        
        form = AuthenticationForm()
    return render(request,'login.html',{'form' : form})     

def watch_video (request,video_id) :
    video = get_object_or_404(Video,pk=video_id)
    related_videos = Video.objects.exclude(pk=video_id)[:10]
    return render(request,'watch.html',{'video' : video,'related_videos' :related_videos})

def like_video (request,video_id) :
    video = get_object_or_404(Video,pk=video_id)
    user = request.user 
    if not user.is_authenticated :
        return JsonResponse({'status' : 'error','message' : 'User Not found'},status=401)
    action = request.POST.get('action') 
    if action == 'like' :
        if user in video.likes.all() :
            video.likes.remove(user) 
            liked = False
        else :
            video.likes.add(user) 
            video.dislikes.remove(user) 
            liked = True
        disliked = user in video.dislikes.all()    
    elif action == 'dislike' :
        if user in video.dislikes.all() :
            video.dislikes.remove(user)
            disliked = False
        else :
            video.dislikes.add(user) 
            disliked = True
            video.likes.remove(user)   
        liked = user in video.likes.all()
    else :
        return JsonResponse({'status': 'error', 'message': 'Invalid action'}, status=400)   
    return JsonResponse({
        'status': 'success',
        'likes_count': video.likes.count(),
        'dislikes_count': video.dislikes.count(),
        'liked': liked,
        'disliked': disliked,
    })       
                       