from django.urls import path
from . import views

urlpatterns = [
    path('todos/', views.todo_list, name='list'),
    path('', views.index, name='home'),
    path('about/', views.about, name='about')
]
