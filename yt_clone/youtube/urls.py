# youtube/urls.py

from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.upload_video, name='upload_video'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
]