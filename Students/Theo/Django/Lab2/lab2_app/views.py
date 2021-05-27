from django.shortcuts import render, redirect
from django.http import HttpResponse


def todo_list(request):
    return render(request, 'todos/todo_list.html')


def index(request):
    return render(request, "pages/index.html")


def about(request):
    return HttpResponse('hello from the about view')
