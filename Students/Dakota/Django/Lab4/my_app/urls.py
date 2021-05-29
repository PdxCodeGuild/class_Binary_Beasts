from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('check_in/', views.check_in, name = 'check_in'),
    path('check_out/', views.check_out, name = 'check_out'),
    path('available_books/', views.available_books, name = 'available_books'),
    path('details/<int:id>', views.see_details, name = 'see_details'),
    path('get_check_in/<int:id>', views.get_check_in, name = 'get_check_in'),
]