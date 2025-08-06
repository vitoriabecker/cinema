from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm, LoginForm, MovieForm, CommentForm
from .models import Movie
from django.utils import timezone


def home(request):
  return render(request, 'cinema/home.html')



#test
'''
def live_stream(request, id):
  movie = get_object_or_404(Movie, id=id)
  now = timezone.now()

  if movie.start_time > now:
    return render(request, 'cinema/home.html', {'movie':movie})
  
  offset = int((now - movie.start_time).total_seconds())
  print('offset in seconds', offset)

  return render(request, 'cinema/movie_detail.html', {'movie':movie, 'offset':offset})
'''


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


#@permission_required('cinema.add_movie', raise_exception=True)
def add_movie(request):
  template_name = 'cinema/add_movie.html'

  #if not request.user.is_superuser():
  #  return redirect('login')

  if request.method == 'POST':
    form = MovieForm(request.POST, request.FILES)

    if form.is_valid():
      movie = form.save(commit=False)

      if 'poster' in request.FILES:
        movie.poster = request.FILES['poster']
      
      movie.save()
      return redirect('movie_list')
    
  else:
    form = MovieForm()
  
  return render(request, template_name, context={'form':form})


def movie_detail(request, id):
  template_name = 'cinema/movie_detail.html'

  """ tenta pegar o objeto do modelo Movie através do id passado, 
      caso nao houver objeto, retorna o erro 404 """
  movie = get_object_or_404(Movie, id=id)
  comments = movie.comments.all()

  comment_form = CommentForm()

  return render(request, template_name, context={'movie':movie,
                                                 'comments':comments,
                                                 'comment_form':comment_form,})


def movie_list(request):
  template_name = 'cinema/movie_list.html'
  movies = Movie.objects.all()
  return render(request, template_name, context={'movies':movies})


#@permission_required('cinema.update_movie', raise_exception=True)
def update_movie(request, id):
  template_name = 'cinema/update_movie.html'

  movie = get_object_or_404(Movie, id=id)

  #if not request.user.is_authenticated or not request.user.is_superuser:
  #  return redirect('login')

  if request.method == 'POST':
    form = MovieForm(request.POST, request.FILES, instance=movie)

    if form.is_valid():
      form.save()
      return redirect('movie_list')
  else:
    form = MovieForm(instance=movie)
  
  return render(request, template_name, context={'form':form})


#@permission_required('cinema.delete_movie', raise_exception=True)
def delete_movie(request, id):
  template_name = 'cinema/delete_movie.html'

  #if not request.user.is_authenticated or not request.user.is_superuser():
  #  return redirect('login')
  
  movie = get_object_or_404(Movie, id=id)

  if request.method == 'POST':
    movie.delete()

    return redirect('movie_list')

  return render(request, template_name, context={'movie':movie})
    


#@login_required
def add_comment_to_movie(request, id):
  template_name = 'cinema/movie_comment.html'

  movie = get_object_or_404(Movie, id=id)

  new_comment = None

  if request.method == 'POST':
    form = CommentForm(request.POST)

    if form.is_valid():
      new_comment = form.save(commit=False) #Create the Comment object, but don’t save it to the database yet
      new_comment.movie = movie
      new_comment.user = request.user
      new_comment.save()
      return redirect('movie_detail', id=id)

  else:
    form = CommentForm()
  return render(request, template_name, context={'movie':movie,
                                                 'new_comment':new_comment,
                                                 'form':form})






