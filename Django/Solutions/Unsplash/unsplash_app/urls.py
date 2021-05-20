from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_images, name = 'get_images'),
    path('add_pictures/<int:id>', views.add_pictures, name = 'add_pictures'),
    path('board/', views.my_board, name = 'board'),

]