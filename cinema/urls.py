from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('movie/', views.movie_list, name='movie_list'),
  path('movie/add', views.add_movie, name='add_movie'),
  path('movie/<int:id>/', views.movie_detail, name='movie_detail'),
  path('movie/<int:id>/update', views.update_movie, name='update_movie'),
  path('movie/<int:id>/delete', views.delete_movie, name='delete_movie'),
  path('movie/<int:id>/comment', views.add_comment_to_movie, name='movie_comment'),
  path('movie/<int:id>/rate', views.rate_movie, name='movie_rate'),
  path('movie/<int:id>/save_movies', views.save_movie, name='save_movie'),

  path('signup/', views.user_signup, name='signup'),
  path('login/', views.user_login, name='login'),
  path('logout/', views.user_logout, name='logout'),
  path('profile/', views.user_profile, name='user_profile'),
  path('change-password/', views.change_password, name='change_password'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)