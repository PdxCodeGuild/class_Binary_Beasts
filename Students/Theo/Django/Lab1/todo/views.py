from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import TodoItem

def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def todo_items(request):
    items = TodoItem.objects.all()  
  
    # creates the context dictionary to send the blog posts to the template
    context = {
       'items': items
    }
    return render(request, 'pages/todo_items.html', context)

def add_items(request):
    if request.method == 'GET': # if its a GET request, just display the add.html template
        return render(request, 'pages/add.html')
    elif request.method == 'POST': # if it's a POST request ..
        description = request.POST['description']   # get the title from the POST submission, this comes from a form
        date_created = request.POST['date_created']
        items = TodoItem.objects.create(description = description, date_created = date_created)
        return redirect('todo_items')