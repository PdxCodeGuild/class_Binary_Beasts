from django.shortcuts import render

posts =  [
    {
        'author': 'John R',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2020'
    },
    {
        'author': 'James S',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 29, 2020'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog_app/home.html', context)

def about(request):
    return render(request, 'blog_app/about.html')