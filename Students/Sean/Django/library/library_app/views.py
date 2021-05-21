from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import book, author
from django.urls import reverse
# Create your views here.
def home(request):
  books = book.objects.all()
  context = {
  "books":books
  }
  return render(request, 'pages/home.html', context)

def borrow(request, id):
  if request.method == 'GET':
    borrow = book.objects.get(pk=id)
    borrow.borrowed = True
    borrow.save()
    return redirect(reverse('home'))

def borrowed(request):
  books = book.objects.all()
  context = {
  "books":books
  }
  return render(request, 'pages/borrowed.html', context)

def unborrow(request, id):
  if request.method == 'GET':
    borrow = book.objects.get(pk=id)
    borrow.borrowed = False
    borrow.save()
    return redirect(reverse('borrowed'))