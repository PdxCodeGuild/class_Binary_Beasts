from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import book, author, History
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import datetime

# Create your views here.

@login_required
def home(request):
  books = book.objects.all()
  context = {
  "books":books
  }
  return render(request, 'pages/home.html', context)

@login_required
def borrow(request, id):
  if request.method == 'GET':
    borrow = book.objects.get(pk=id)
    borrow.borrowed = True
    borrow.save()

    user = request.user
    History.objects.create(book=borrow, user=user)
    return redirect(reverse('home'))

@login_required
def borrowed(request):
  books = book.objects.all()
  context = {
  "books":books
  }
  return render(request, 'pages/borrowed.html', context)

@login_required
def unborrow(request, id):

  borrow = book.objects.get(pk=id)
  borrow.borrowed = False
  borrow.save()

  time_now = datetime.datetime.now()
  times = borrow.history_set.all()
  history_update = times.last()
  history_update.returned = time_now
  history_update.save()
  return redirect(reverse('borrowed'))