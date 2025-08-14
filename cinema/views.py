from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .forms import MovieForm, CommentForm, RatingForm
from .models import Movie, Rating
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


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
  user_rating = Rating.objects.filter(rating=0).order_by("?").first()
  comments = movie.comments.all()

  rating_form = RatingForm()
  comment_form = CommentForm()

  return render(request, template_name, context={'movie':movie,
                                                 'comments':comments,
                                                 'user_rating':user_rating,
                                                 'rating_form': rating_form,
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
      return redirect('movie_detail', id=id)
  else:
    form = MovieForm(instance=movie)
  
  return render(request, template_name, context={'form':form, 'movie':movie})


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


def rate_movie(request, id):
  template_name = 'movie_detail.html'

  movie = get_object_or_404(Movie, id=id)

  if request.method == 'POST':
    form = RatingForm(request.POST, instance=user_rating)

    if form.is_valid():
      user_rating = form.save(commit=False) # cria o objeto rating, mas ainda não salva no DB. 
                                            # é preciso fazer isso pq o objeto depende de outros campos, como movie e user
                                            # então eu adiciono eles manualmente, e ai sim eu salvo o objeto no DB.
      user_rating.movie = movie
      user_rating.user = request.user
      user_rating.save()
      return redirect('movie_detail', id=id)
    
  else:
    form = RatingForm(instance=user_rating)
  
  return render(request, template_name, context={'movie':movie,
                                                 'user_rating':user_rating, 
                                                 'form':form})






