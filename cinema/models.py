from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

# eu retirei o model User, pq eu estou usando o User do django
# comparar isso com meu outro projeto e ver como aplicar o User do django nos forms

class Movie(models.Model):
  title = models.CharField(max_length=140, blank=True, null=True)
  year = models.CharField(max_length=4, blank=True, null=True)
  length = models.CharField(max_length=4, blank=True, null=True)
  genre = models.CharField (max_length=40)
  director = models.CharField(max_length=130)
  synopsis = models.TextField(max_length=4, blank=True, null=True)
  poster = models.ImageField(upload_to='media/posters', null=True)

  # video_file = 
  # start_time = 

  def __str__(self):
    return self.title
  
  def get_absolute_url(self):
    return reverse('movie_detail', kwargs={'pk':self.pk})
  
  # def is_live(self):
  


class Comment(models.Model):
  user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
  movie = models.ForeignKey(Movie, related_name='comments', on_delete=models.CASCADE)
  text = models.TextField
  created_date = models.TimeField(default=timezone.now())
