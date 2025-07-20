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
@login_required(login_url='login.html')
def watch_video (request,video_id) :
    video = get_object_or_404(Video,pk=video_id)
    user = request.user
    if request.method == 'POST' :
        form = CommentForm(request.POST) 
        if form.is_valid() :
            comment = form.save(commit=False)
            comment.video = video
            comment.channel = Channel.objects.get(user=user) 
            comment.save()
            return redirect('watch_video',video_id=video.pk)
    else :
        form = CommentForm()
        comments = video.comments.all() 
        if user not in video.views.all() :
            video.views.add(user)
        related_videos = Video.objects.exclude(pk=video_id)[:10]
        
        # Check if the current user is subscribed to the video's channel
        is_subscribed = False
        if request.user.is_authenticated and hasattr(request.user, 'channel'):
            user_channel = request.user.channel
            if user_channel in video.channel.subscribers.all():
                is_subscribed = True

        context = {
            'video': video,
            'related_videos': related_videos,
            'form': form, # Pass the form to the template
            'comments': comments, # Pass comments to the template
            'is_subscribed': is_subscribed, # Pass subscription status
        }
        return render(request,'watch.html',context)

@login_required(login_url='login.html')
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


@login_required(login_url='login.html')
def like_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    user = request.user

    if not user.is_authenticated:
        return JsonResponse({'status': 'error', 'message': 'User Not found'}, status=401)

    if user in comment.likes.all():
        comment.likes.remove(user)
        liked = False
    else:
        comment.likes.add(user)
        if user in comment.dislikes.all():
            comment.dislikes.remove(user)
        liked = True

    return JsonResponse({
        'status': 'success',
        'liked': liked,
        'likes_count': comment.likes.count(),
        'dislikes_count': comment.dislikes.count()
    })

@login_required(login_url='login.html')
def dislike_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    user = request.user

    if not user.is_authenticated:
        return JsonResponse({'status': 'error', 'message': 'User Not found'}, status=401)

    if user in comment.dislikes.all():
        comment.dislikes.remove(user)
        disliked = False
    else:
        comment.dislikes.add(user)
        disliked = True
        if user in comment.likes.all():
            comment.likes.remove(user)
            
    return JsonResponse({
        'status': 'success',
        'disliked': disliked,
        'likes_count': comment.likes.count(),
        'dislikes_count': comment.dislikes.count()
    })

@login_required(login_url='login.html')
def subscribe(request, channel_id):
    target_channel = get_object_or_404(Channel, pk=channel_id)
    user_channel = request.user.channel # Assuming user has a one-to-one Channel relationship

    if not user_channel:
        return JsonResponse({'status': 'error', 'message': 'User does not have a channel.'}, status=400)

    if user_channel == target_channel:
        return JsonResponse({'status': 'error', 'message': 'Cannot subscribe to your own channel.'}, status=400)

    is_subscribed = False
    if user_channel in target_channel.subscribers.all(): # Corrected logic
        target_channel.subscribers.remove(user_channel)
        is_subscribed = False
    else:
        target_channel.subscribers.add(user_channel)
        is_subscribed = True
    
    # Get the next URL from the request, if available
    next_url = request.GET.get('next', request.POST.get('next'))
    if next_url:
        return redirect(next_url)

    return JsonResponse({
        'status': 'success',
        'is_subscribed': is_subscribed,
        'subscribers_count': target_channel.subscribers.count()
    })
