from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Todo
from django.urls import reverse

def home(request):
  todos = Todo.objects.all()
  context = {
    "todos":todos
  }
  return render(request, 'pages/home.html', context)

def add_post(request):
  if request.method == 'GET':
    return render(request, 'pages/add.html')
  elif request.method == 'POST':
    title = request.POST['title']
    pub_date = request.POST['pub_date']
    due_date = request.POST['due_date']

    Todo.objects.create(title = title, pub_date = pub_date, due_date = due_date)
    return redirect('home')

def delete(request, id):
  if request.method == 'GET':
    Todo.objects.get(pk=id).delete()
    return redirect('home')

def edit(request, id):
  if request.method == 'GET':
    edited = Todo.objects.get(pk=id)
    context = {
      'edited':edited
      }
    return render(request, 'pages/edit.html', context)

def replace(request, id):
  replacer = Todo.objects.get(pk=id)
  replacer.title = request.POST['title']
  replacer.pub_date = request.POST['pub_date']
  replacer.due_date = request.POST['due_date']
  replacer.save()

  todos = Todo.objects.all()
  context = {
    "todos":todos
  }
  return render(request, 'pages/home.html', context)