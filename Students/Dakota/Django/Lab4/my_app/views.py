from django.shortcuts import render, redirect
from .models import Book, Author, CheckedOut
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'pages/home.html')
@login_required
def check_in(request):
    if request.method == 'GET':
        books = Book.objects.filter(user=request.user)
        context = {
            'books':books
        }
        return render(request, 'pages/check_in.html', context)
    elif request.method == 'POST':
        user = request.user
        title = request.POST['title']
        author = request.POST['author']
        pub_date = request.POST['pub_date']
        authorName = Author.objects.create(author = author)
        Book.objects.create(title = title, pub_date = pub_date, user=user, author=authorName)
        return redirect('available_books')

def get_check_in(request, id):
    # if request.method == 'GET':
    getBooks = Book.objects.filter(user=request.user)
    context = {
        'getBooks':getBooks
    }
    getbook = Book.objects.get(id = id)
    getbook.checkout = False
    getbook.save()
    return redirect('check_in')

@login_required
def check_out(request):
    if request.method == 'GET':
        books = Book.objects.filter(user=request.user)
        context = {
            'books':books
        }
        return render(request, 'pages/check_out.html', context)
    elif request.method == 'POST':
        user = request.user
        book = Book.objects.all().filter(title=request.POST['book']).first()
        book.checkout = True
        book.save()
        CheckedOut.objects.create(book = book, user=user)
        print(book)
        return redirect('available_books')

@login_required
def available_books(request):
    Books = Book.objects.filter(user=request.user)
    context = {
        'Books':Books
    }
    return render(request, 'pages/available_books.html', context)
@login_required
def see_details(request, id):
    post = Book.objects.get(id=id)
    return render(request, 'pages/details.html', {"post": post})

#switch HTML for check in to get book
#create a new view that works with the new Get Form

