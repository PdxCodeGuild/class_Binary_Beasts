from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('check_book/', views.check_book, name = 'check_book'),
    path('checkout/', views.checkout, name = 'checkout'),
    path('checkin/', views.checkin, name = 'checkin'),
    path('history/', views.history, name = 'history'),


]