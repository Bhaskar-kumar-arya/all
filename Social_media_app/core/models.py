from django.db import models
from django.contrib.auth import get_user_model
import uuid 
from datetime import datetime

User = get_user_model()

# Create your models here.
class Profile (models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profileimg = models.ImageField(upload_to='profile_images',default="def_user.jpeg")
    location = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.user.username
    
class Post (models.Model) :
    id = models.UUIDField(primary_key=True,default = uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="posts_images")
    caption = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    no_of_likes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username}'s post"

class LikePost(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta :
        unique_together = ('post','user')

class FollowersCount (models.Model) :
    follower = models.ForeignKey(User,related_name="following",on_delete=models.CASCADE)
    user = models.ForeignKey(User,related_name="followers",on_delete=models.CASCADE)

    def __str__(self):
        return self.user + " follows " + self.follower

