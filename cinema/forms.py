from django import forms
from .models import User, Movie, Comment
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField

class SignUpForm(UserCreationForm):
  class Meta: 
    model = User
    fields = ('fname','lname','email','password')
    labels = {'fname':'Primeiro nome', 'lname':'Sobrenome', 'email':'E-mail',
              'password':'Senha'} 

class LoginForm(AuthenticationForm):
  username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True}))
  password = forms.CharField(label= 'Password', widget=forms.PasswordInput(attrs={'autocomplete':'current-password'}))

class MovieForm(forms.Form):
  class Meta:
    model = Movie
    fields = ('title','year','length','genre','director','synopsis','poster')
    labels = {'title':'Título','year':'Ano','length':'Duração','genre':'Gênero',
              'director':'Diretor(a)','synopsis':'Sinopse','poster':'Pôster'}
    
class CommentForm(forms.Form):
  class Meta:
    model = Comment
    fields = ('text')