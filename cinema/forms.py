from django import forms
from .models import Movie, Profile, Comment, Rating
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm


class SignUpForm(UserCreationForm):
  class Meta: 
    fields = ['name','email','password']
    labels = {'name':'Nome', 'email':'E-mail', 'password':'Senha'} 


class LoginForm(AuthenticationForm):
  username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True}))
  password = forms.CharField(label= 'Password', widget=forms.PasswordInput(attrs={'autocomplete':'current-password'}))


class UpdateProfileForm(forms.ModelForm):
  avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
  bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

  class Meta:
    model = Profile
    fields = ['avatar', 'bio']


class MovieForm(forms.ModelForm):
  class Meta:
    model = Movie
    fields = ['title','year','length','genre','director','synopsis','poster',]
    
    widgets = {
      'title': forms.TextInput(attrs={'class': 'form-control'}),
      'year': forms.TextInput(attrs={'class': 'form-control'}),
      'length': forms.TextInput(attrs={'class': 'form-control'}),
      'genre': forms.TextInput(attrs={'class': 'form-control'}),
      'director': forms.TextInput(attrs={'class': 'form-control'}),
      'synopsis': forms.Textarea(attrs={'class': 'form-control'}),
    }
    
class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ['text',]

class RatingForm(forms.ModelForm):
  class Meta:
    model = Rating
    fields = ['score',]