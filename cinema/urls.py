from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  
  path('live/', views.live_stream, name='live_stream'),

  path('movie/', views.movie_list, name='movie_list'),
  path('movie/add', views.add_movie, name='add_movie'),
  path('movie/<int:id>/', views.movie_detail, name='movie_detail'),
  path('movie/<int:id>/update', views.update_movie, name='update_movie'), # ou movie/update/<int:pk> ??
  path('movie/<int:id>/delete', views.delete_movie, name='delete_movie'),
  path('movie/<int:id>/comment', views.add_comment_to_movie, name='add_comment_to_movie'),

  path('signup/', views.user_signup, name='signup'),
  path('login/', views.user_login, name='login'),
  path('logout/', views.user_logout, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)