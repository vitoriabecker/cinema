from django.db import models
from PIL import Image
from django.urls import reverse
from django.contrib.auth.models import User

class Movie(models.Model):
  title = models.CharField(max_length=140, blank=True, null=True)
  year = models.CharField(max_length=4, blank=True, null=True)
  length = models.CharField(max_length=4, blank=True, null=True)
  genre = models.CharField (max_length=40)
  director = models.CharField(max_length=130)
  synopsis = models.TextField(max_length=255, blank=True, null=True)
  poster = models.ImageField(upload_to='media/posters', null=True)

  def __str__(self):
    return self.title
  
  def get_absolute_url(self):
    return reverse('movie_detail', kwargs={'pk':self.pk})
  

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  avatar = models.ImageField(upload_to='media/avatar', null=True)
  bio = models.TextField(max_length=255, blank=True, null=True)
  saved_movies = models.ManyToManyField(Movie, blank=True, related_name='saved_by')

  def __str__(self):
    return self.user.username
  
  def save(self, *args, **kwargs):
    super().save()

    img = Image.open(self.avatar.path)

    if img.height > 100 or img.width > 100:
        new_img = (100, 100)
        img.thumbnail(new_img)
        img.save(self.avatar.path)
  

class Comment(models.Model):
  user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
  movie = models.ForeignKey(Movie, related_name='comments', on_delete=models.CASCADE)
  text = models.TextField(default='write a comment')
  created_date = models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering = ['created_date']

  def __str__(self):
    return 'Comment {} by {}'.format(self.text, self.user)
  

class Rating(models.Model):
  user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
  movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
  score = models.FloatField(default=0)

  class Meta:
    constraints = [
        models.UniqueConstraint(fields=['user', 'movie'], name='unique_user_movie')
    ]
    
  def __str__(self):
    return '{}: {}'.format(self.movie.title, self.score)
  
