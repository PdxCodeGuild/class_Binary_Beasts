from django.shortcuts import redirect, render
from .models import Book, History
from django.utils import timezone

def home(request):
    return render(request, 'pages/home.html')

def check_book(request):
    out_list = Book.objects.filter(available=False)
    in_list = Book.objects.filter(available=True)
    context = {
        'out_list' : out_list,
        'in_list' : in_list
    }
    return render(request, 'pages/check_book.html', context)

def checkout(request):
    book = Book.objects.get(pk= request.POST['books'])
    book.available = False
    book.save()
    user = request.POST['name']
    createEntry(book, user, True)
    return redirect('check_book')

def checkin(request):
    book = Book.objects.get(pk= request.POST['books'])
    book.available = True
    book.save()
    user = request.POST['name']
    createEntry(book, user, False, )
    return redirect('check_book')

def history(request):
    history = History.objects.all()
    context = {
        'history' : history,
    }
    return render(request, 'pages/history.html', context)

def createEntry(book, user, checkout):
    History.objects.create(book = book, user = user, checkout = checkout, timestamp = timezone.now())
