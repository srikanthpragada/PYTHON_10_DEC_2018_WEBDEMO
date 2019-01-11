from django.shortcuts import render, redirect
from .forms import AddBookForm, OrmAddBookForm
import sqlite3
from .models import Book
from django.http import JsonResponse, HttpResponse
from django.db.models import Avg


def list_books(request):
    books = Book.objects.all()
    return render(request, 'orm_list_books.html', {'books': books})


def add_book(request):
    if request.method == "GET":
        f = OrmAddBookForm()
        return render(request, 'orm_add_book.html', {'form': f})
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
    # Get selected Book objects converted to dict using values()
    books = Book.objects.filter(title__contains=title).values()
    bookslist = list(books)  # Convert QuerySet to list
    return JsonResponse(bookslist, safe=False)


def home_books(request):
    return render(request, 'orm_home_books.html')


def books_summary(request):
    summary = Book.objects.all().aggregate(avg_price=Avg('price'))
    avg = summary['avg_price']
    return HttpResponse(f"Average Price : {avg}")
