from django.shortcuts import render, redirect
from .models import url
from .forms import Url
import string
import random


def home(request):
    urlLists = url.objects.all()
    context = {
        'urlLists': urlLists
    }
    return render(request, 'pages/home.html', context)


def addURL(request):
    content = request.POST['content']
    request.method == 'POST'
    allURL = url.objects.create(urlItem=content)
    new_url = ''
    for i in range(15):
        letter = random.choice(string.ascii_letters)
        new_url += letter
    new_url += ".com"
    allURL.shortURL = new_url
    allURL.save()
    return redirect('home')


def urlRedirect(request, id):
    data = url.objects.get(id=id)
    return redirect(data.urlItem)
