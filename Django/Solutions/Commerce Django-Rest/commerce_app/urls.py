from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('api/products/', views.product_list),
    path('api/products/<int:pk>', views.product_detail),
    path('', views.home, name='home')
]

urlpatterns = format_suffix_patterns(urlpatterns)
