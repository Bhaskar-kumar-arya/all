from django import forms
from .models import Video
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'media', 'thumbnail']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter video title', 'class': 'your-css-class'}),
            'description': forms.Textarea(attrs={'placeholder': 'Tell viewers about your video', 'rows': 5, 'class': 'your-css-class'}),
        }

class RegisterForm (UserCreationForm)  :
    channel_name = forms.CharField(max_length=20,label='Channel Name')
    class Meta :
        model = User
        fields = ['username','password1','password2','channel_name']
