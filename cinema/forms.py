from django import forms
from .models import Movie, Profile, Comment, Rating
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm


class RegistrationForm(UserCreationForm):

  email = forms.EmailField()
  first_name = forms.CharField(label="Primeiro nome")
  last_name = forms.CharField(label="Sobrenome")

  class Meta:
    model = User
    fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

    ## Por algum motivo o field usuario é o unico renderizando certo, verificar isso amanha
    widgets = {
      'first_name': forms.TextInput(attrs={'class': 'w-full h-10 px-3 py-2 text-sm text-neutral-100 border border-neutral-700 rounded-lg mb-2'}),
      'last_name': forms.Textarea(attrs={'class': 'w-full h-10 px-3 py-2 text-sm text-neutral-100 border border-neutral-700 rounded-lg mb-2'}),
      'username': forms.TextInput(attrs={'class': 'w-full h-10 px-3 py-2 text-sm text-neutral-100 border border-neutral-700 rounded-lg mb-2'}),
      'email': forms.EmailInput(attrs={'class': 'w-full h-10 px-3 py-2 text-sm text-neutral-100 border border-neutral-700 rounded-lg mb-2'}),
      'password1': forms.PasswordInput(attrs={'class': 'w-full h-10 px-3 py-2 text-sm text-neutral-100 border border-neutral-700 rounded-lg mb-2'}),
      'password2':forms.PasswordInput(attrs={'class': 'w-full h-10 px-3 py-2 text-sm text-neutral-100 border border-neutral-700 rounded-lg mb-2'}),
    }


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
    fields = ['title', 'poster', 'year','length','genre','director','synopsis',]
    
    widgets = {
      'title': forms.TextInput(attrs={'class': 'w-full h-10 px-3 py-2 text-sm text-neutral-100 border border-neutral-700 rounded-lg mb-2'}),
      'poster': forms.FileInput(attrs={'class': 'w-full h-10 text-neutral-500 text-sm border border-neutral-700 file:cursor-pointer cursor-pointer file:py-2.5 file:px-3 file:mr-4 file:bg-neutral-700 file:hover:bg-gray-700 file:text-white rounded-lg mb-2'}),
      'year': forms.TextInput(attrs={'class': 'w-full h-10 px-3 py-2 text-sm text-neutral-100 border border-neutral-700 rounded-lg mb-2'}),
      'length': forms.TextInput(attrs={'class': 'w-full h-10 px-3 py-2 text-sm text-neutral-100 border border-neutral-700 rounded-lg mb-2'}),
      'genre': forms.TextInput(attrs={'class': 'w-full h-10 px-3 py-2 text-sm text-neutral-100 border border-neutral-700 rounded-lg mb-2'}),
      'director': forms.TextInput(attrs={'class': 'w-full h-10 px-3 py-2 text-sm text-neutral-100 border border-neutral-700 rounded-lg mb-2'}),
      'synopsis': forms.Textarea(attrs={'class': 'w-full h-28 px-3 py-2 text-sm text-neutral-100 border border-neutral-700 rounded-lg mb-2'}),
    }
    
class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ['text']

    widgets = {
      'text': forms.Textarea(attrs={
        'class': 'w-full h-28 px-7 py-6 text-sm text-neutral-100 rounded-2xl bg-neutral-900',
        'placeholder': 'Escreva um comentário...',
      }),
    }

class RatingForm(forms.ModelForm):
  class Meta:
    model = Rating
    fields = ['score',]