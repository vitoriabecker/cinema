from django.contrib import admin
from .models import Movie, Profile, Comment, Rating

admin.site.register(Movie)
admin.site.register(Profile)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
  list_display = ['user', 'text', 'movie', 'created_date']
  list_filter = ['created_date']
  search_fields = ('user', 'text')

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
  list_display = ['user', 'movie', 'score']

