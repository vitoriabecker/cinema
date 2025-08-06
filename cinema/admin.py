from django.contrib import admin
from .models import Movie, Comment

admin.site.register(Movie)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
  list_display = ['user', 'text', 'movie', 'created_date']
  list_filter = ['created_date']
  search_fields = ('user', 'text')

