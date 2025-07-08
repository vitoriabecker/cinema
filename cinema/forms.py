from django import forms
from .models import User, Movie, Comment
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField

class SignUpForm(UserCreationForm):
  class Meta: 
    fields = ('fname','lname','email','password')
    labels = {'fname':'Primeiro nome', 'lname':'Sobrenome', 'email':'E-mail',
              'password':'Senha'} 

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
    
class CommentForm(forms.Form):
  class Meta:
    model = Comment
    fields = ('text')