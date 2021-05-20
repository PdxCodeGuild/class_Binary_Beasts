from django.urls import path, re_path
from . import views 
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from django.conf import settings



urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('shorten_url/', views.shorten_url, name = 'shorten_url'),
    path(
        "favicon.ico", 
        RedirectView.as_view(url=staticfiles_storage.url("favicon.ico"))),
    path('<path:resource>', views.redirect_to_link, name = 'redirect_to_link'),
]