# youtube/urls.py

from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.upload_video, name='upload_video'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('watch/<int:video_id>',views.watch_video,name='watch_video'),
    path('video/<int:video_id>/like/', views.like_video, name='like_video'),
    path('comment/<int:comment_id>/like/', views.like_comment, name='like_comment'),
    path('comment/<int:comment_id>/dislike/', views.dislike_comment, name='dislike_comment'),
    path('channel/<int:channel_id>/subscribe/', views.subscribe, name='subscribe'),
]