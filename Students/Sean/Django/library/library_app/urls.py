from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('borrow/<int:id>', views.borrow, name='borrow'),
  path('unborrow/<int:id>', views.unborrow, name='unborrow'),
  path('borrowed/', views.borrowed, name='borrowed'),
]