from django.shortcuts import render, redirect
from .models import TodoItem

def home(request):
    items = TodoItem.objects.all()
    context = {
        'items': items
    }
    return render(request, 'pages/home.html', context)


def add_item(request):
    text = request.POST['text']
    pub_date = request.POST['pub_date']
    item = TodoItem.objects.create(text = text, pub_date = pub_date)
    return redirect('home')


def details(request, id):
    item = TodoItem.objects.get(pk=id)

    context = {
        'item' : item
    }

    return render(request, 'pages/details.html', context)
