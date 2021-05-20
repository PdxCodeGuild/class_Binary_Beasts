from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name = 'home'),
    path('addURL/', views.addURL, name = 'addURL'),
    path('<int:id>', views.urlRedirect, name="urlRedirect")
]