from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'blog_app/index.html')

def about(request):
    return HttpResponse('<h1>About</h1>')