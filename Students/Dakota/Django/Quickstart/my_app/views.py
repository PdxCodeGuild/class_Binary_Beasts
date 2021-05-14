from django.shortcuts import render, redirect
from .models import Blog
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'pages/home.html')

@login_required
def about(request):
    return render(request, 'pages/about.html') 

@login_required
def add_post(request):
    if request.method == 'GET':
        return render(request, 'pages/add.html')
    elif request.method == 'POST':
        user = request.user
        title = request.POST['title']
        text = request.POST['text']
        pub_date = request.POST['pub_date']
        Blog.objects.create(title = title, text = text, pub_date = pub_date, user=user)
        return redirect('home')

@login_required
def blog_posts(request):
    blogs = Blog.objects.filter(user=request.user)
    context = {
        'blogs':blogs
    }
    return render(request, 'pages/posts.html', context)

@login_required
def see_details(request, id):
    post = Blog.objects.get(id=id)
    return render(request, 'pages/details.html', {"post": post})