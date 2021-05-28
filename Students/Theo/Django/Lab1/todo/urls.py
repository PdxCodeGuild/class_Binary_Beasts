from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('todo_items/', views.todo_items, name = 'todo_items'),
    path('add/', views.add_items, name = 'add_items')
]