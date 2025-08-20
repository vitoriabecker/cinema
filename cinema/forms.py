from django import forms
from .models import Movie, Comment, Rating
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField

class SignUpForm(UserCreationForm):
  class Meta: 
    fields = ('name','email','password')
    labels = {'name':'Nome', 'email':'E-mail', 'password':'Senha'} 

class LoginForm(AuthenticationForm):
  username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True}))
  password = forms.CharField(label= 'Password', widget=forms.PasswordInput(attrs={'autocomplete':'current-password'}))

class MovieForm(forms.ModelForm):
  class Meta:
    model = Movie
    fields = ('title','year','length','genre','director','synopsis','poster')
    
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