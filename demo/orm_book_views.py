from django.shortcuts import render, redirect
from .forms import AddBookForm, OrmAddBookForm
import sqlite3
from . models import Book
from django.http import JsonResponse


def list_books(request):
    books = Book.objects.all()
    return render(request, 'orm_list_books.html', {'books': books})


def add_book(request):
    if request.method == "GET":
        f = OrmAddBookForm()
        return render(request, 'orm_add_book.html',{'form' : f})
    else:
        f = OrmAddBookForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect("/demo/orm/listbooks")
        else:
            return render(request, 'orm_add_book.html', {'form': f})


def delete_book(request):
    id = request.GET["id"]
    book = Book.objects.get(id=id)
    book.delete()
    return redirect("/demo/orm/listbooks")

def search_books(request):
    return render(request, 'orm_search_books.html')


def get_books(request):
    title = request.GET['title']
    books = Book.objects.all().values()
    bookslist = list(books)   # Convert QuerySet to list
    return JsonResponse(bookslist, safe=False)
