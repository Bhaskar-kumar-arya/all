from django.db import models
from django.contrib.auth.models import User

# Create your models here.
    
class Channel (models.Model) :
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    profile_picture = models.ImageField(upload_to='channel_profile_pics/',default='newVideo.jpeg')
    subscribers = models.ManyToManyField('Channel',related_name='channel_subscribers',blank=True)
    def __str__(self):
        return f"Channel of {self.user.username}"

class Video (models.Model) :
    channel = models.ForeignKey(Channel,on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=50) 
    media = models.FileField(upload_to='Videos/')
    thumbnail = models.ImageField(upload_to='thumbnails/',default='newVideo.jpeg')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    views = models.ManyToManyField(User,related_name='watched_videos',blank=True)
    likes = models.ManyToManyField(User,related_name='liked_videos',blank=True)
    dislikes = models.ManyToManyField(User,related_name='disliked_videos',blank=True)

    def  __str__(self):
        return f"Video : Title = {self.title} of self.channel.user.username" 
    
class Comment (models.Model) :
    channel = models.ForeignKey(Channel,on_delete=models.CASCADE,related_name='comments') 
    video = models.ForeignKey(Video,on_delete=models.CASCADE,related_name='comments')
    text = models.TextField(max_length=255)
    likes = models.ManyToManyField(User, related_name='liked_comments', blank=True)
    dislikes = models.ManyToManyField(User, related_name='disliked_comments', blank=True)

    def __str__(self):
        return f"comment by {self.channel.name} , on video {self.video.title}"  