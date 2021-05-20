from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('add/', views.add_post, name='add'),
  path('delete/<int:id>', views.delete, name='delete'),
  path('edit/<int:id>', views.edit, name='edit'),
  path('replace/<int:id>', views.replace, name='replace'),
]