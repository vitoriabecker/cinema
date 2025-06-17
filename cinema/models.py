from django.db import models
from django.utils import timezone
from django.urls import reverse


class User(models.Model):
  fname = models.CharField(max_length=40)
  lname = models.CharField(max_length=120)
  email = models.EmailField(max_length=50)
  password = models.CharField(max_length=10)

  def __str__(self):
    return self.fname
  

class Movie(models.Model):
  title = models.CharField
  year = models.CharField(max_length=4, blank=True, null=True)
  length = models.CharField
  genre = models.CharField (max_length=40)
  director = models.CharField(max_length=130)
  synopsis = models.TextField
  poster = models.ImageField(upload_to='media/posters', null=True)

  def __str__(self):
    return self.title
  
  def get_absolute_url(self):
    return reverse('movie_detail', kwargs={'pk':self.pk})


class Comment(models.Model):
  user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
  movie = models.ForeignKey(Movie, related_name='comments', on_delete=models.CASCADE)
  text = models.TextField
  created_date = models.TimeField(default=timezone.now())
