from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm, LoginForm, MovieForm, CommentForm

def home(request):
  return render(request, 'cinema/home.html')


def user_signup(request):
  template_name = 'signup.html'

  if request.method == 'POST':
    form = SignUpForm(request.POST)

    if form.is_valid():
      username = form.cleaned_data['username']
      password = form.cleaned_data['password']
      user = User.objects.create_user(username=username, password=password)
      login(request, user)

      return redirect('home')
    
  else:
    form = SignUpForm()

  return render(request, template_name, context={'form':form})


def user_login(request):
  template_name = 'login.html'

  if request.method == 'POST':
    form = LoginForm(request.POST)

    if form.is_valid():
      user = authenticate(
        username = form.cleaned_data['username'],
        password = form.cleaned_data['password']
      )

      if user is not None:
        login(request, user)
        return redirect('home')
      else:
        form.add_error(None, 'Invalid username or password.')
  
  else:
    form = LoginForm()

  return render(request, template_name, context={'form':form})


def user_logout(request):
  logout(request)
  return redirect('home')


def add_movie(request):
  template_name = 'add_movie.html'

  if request.method == 'POST':
    form = MovieForm(request.POST, request.FILES)

    if form.is_valid():
      form.save()
      return redirect('movie_list')

  else:
    form = MovieForm()
    
  return render(request, template_name, context={'form':form})


def movie_list(request):
  pass

def update_movie(request):
  pass

def delete_movie(request):
  pass

def movie_detail(request):
  pass

def add_comment_to_movie(request):
  pass
