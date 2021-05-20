from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('add/', views.add_post, name='add_posts'),
  path('posts/', views.blog_posts, name='posts'),
  path('details/<int:id>', views.see_details, name='see_details'),
]