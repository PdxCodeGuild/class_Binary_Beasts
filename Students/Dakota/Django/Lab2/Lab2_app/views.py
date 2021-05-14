from django.shortcuts import render, redirect
from .models import TodoList
from django.http import HttpResponseRedirect
from django.urls import reverse


def home(request):
    lists = TodoList.objects.all()
    context = {
        'lists': lists
    }
    return render(request, 'pages/home.html', context)


def add(request):
    content = request.POST['content']
    request.method == 'POST'
    TodoList.objects.create(listItem=content).save()
    return HttpResponseRedirect(reverse('home'))

def delete(request, id):
    TodoList.objects.get(pk=id).delete()
    return HttpResponseRedirect(reverse('home'))