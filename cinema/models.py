from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
import datetime

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

  #test
  video_url = models.URLField(null=True, blank=True)
  start_time = models.DateTimeField(default=timezone.now())


  def __str__(self):
    return self.title
  
  def get_absolute_url(self):
    return reverse('movie_detail', kwargs={'pk':self.pk})
  
  #test
  def is_live(self):
    now = timezone.now()
    return self.start_time <= now <= self.end_time
  
  def end_time(self):
    return self.start_time + self.duration()
  
  def duration(self):
    return timezone.timedelta(minutes=120)
  

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