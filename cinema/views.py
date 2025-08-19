from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .forms import MovieForm, CommentForm, RatingForm
from .models import Movie, Rating
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test


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
  template_name = 'registration/signup.html'

  if request.method == 'POST':
    form = UserCreationForm(request.POST)

    if form.is_valid():
      form.save()
      return redirect('home')
    
  else:
    form = UserCreationForm()

  return render(request, template_name, context={'form':form})


def user_login(request):
  template_name = 'registration/login.html'
  form = AuthenticationForm()

  if request.method == 'POST':
    form = AuthenticationForm(request.POST)

    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(request, username=username, password=password)

    if user is not None:
      login(request, user)
      return redirect('home')
    else:
      messages.error(request, 'Invalid username or password.')
  
  return render(request, template_name, context={'form':form})


@login_required #ta certo isso? ou coloco apenas na template?
def user_logout(request):
  logout(request)
  return redirect('home')


@user_passes_test(lambda u: u.is_superuser) # redireciono para login com uma mensagme ou deixo como page not found?
def add_movie(request):
  template_name = 'cinema/add_movie.html'

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
  movie = get_object_or_404(Movie, id=id)

  user_rating = None

  if request.user.is_authenticated:
    user_rating = Rating.objects.filter(movie=movie, user=request.user).first()

  comments = movie.comments.all()
  comment_form = CommentForm()
  rating_form = RatingForm()

  return render(request, template_name, context={'movie':movie,
                                                 'comments':comments,
                                                 'comment_form':comment_form,
                                                 'user_rating':user_rating,
                                                 'rating_form': rating_form,})


def movie_list(request):
  template_name = 'cinema/movie_list.html'

  movies = Movie.objects.all()
  return render(request, template_name, context={'movies':movies})


@user_passes_test(lambda u: u.is_superuser, login_url='login')
def update_movie(request, id):
  template_name = 'cinema/update_movie.html'
  
  movie = get_object_or_404(Movie, id=id)

  if request.method == 'POST':
    form = MovieForm(request.POST, request.FILES, instance=movie)

    if form.is_valid():
      form.save()
      return redirect('movie_detail', id=id)
  else:
    form = MovieForm(instance=movie)
  
  return render(request, template_name, context={'form':form, 'movie':movie})


@user_passes_test(lambda u: u.is_superuser, login_url='login')
def delete_movie(request, id):
  template_name = 'cinema/delete_movie.html'
  
  movie = get_object_or_404(Movie, id=id)

  if request.method == 'POST':
    movie.delete()

    return redirect('movie_detail', id=id)

  return render(request, template_name, context={'movie':movie})
    

@login_required
def add_comment_to_movie(request, id):
  movie = get_object_or_404(Movie, id=id)

  if request.method == 'POST':
    print('fon')
    comment_form = CommentForm(request.POST)

    if comment_form.is_valid():
      new_comment = comment_form.save(commit=False)
      new_comment.movie = movie
      new_comment.user = request.user 
      new_comment.save()
      return redirect('movie_detail', id=id)
    else:
      return redirect('movie_list')
  return redirect('movie_detail', id=id)


@login_required
def rate_movie(request, id):
  template_name = 'cinema/movie_detail.html'

  movie = get_object_or_404(Movie, id=id)

  if request.method == 'POST':
      rating = request.POST.get('rating')

      existing_rating = Rating.objects.filter(movie=movie, user=request.user).first()

      if existing_rating:
        existing_rating.rating = rating
        existing_rating.save()
      else:
        new_rating = Rating(rating=rating, movie=movie, user=request.user)
        new_rating.save()

      return redirect('movie_detail', id=id)   
   
  return render(request, template_name, context={'movie':movie})






