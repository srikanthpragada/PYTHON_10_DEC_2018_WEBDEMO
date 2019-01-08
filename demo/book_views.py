from django.shortcuts import render, redirect
from .forms import AddBookForm
import sqlite3


def list_books(request):
    con = sqlite3.connect(r"e:\classroom\python\dec10\library.db")
    cur = con.cursor()
    cur.execute("select * from books order by id")
    books = cur.fetchall()
    con.close()
    return render(request, 'list_books.html', {'books': books})


def add_book(request):
    if request.method == "GET":
        f = AddBookForm()
        return render(request, 'add_book.html', {'form': f})
    else:  # Post
        f = AddBookForm(request.POST)  # Bind request data with form
        if f.is_valid():
            title = f.cleaned_data['title']
            author = f.cleaned_data['author']
            price = f.cleaned_data['price']
            # insert row into table
            con = sqlite3.connect(r"e:\classroom\python\dec10\library.db")
            cur = con.cursor()
            cur.execute("insert into books(title,author,price) values(?,?,?)",
                        (title, author, price))
            if cur.rowcount == 1:
                con.commit()
                con.close()
                return redirect("/demo/listbooks")

        return render(request, 'add_book.html', {'form': f})


def delete_book(request):
    id = request.GET["id"]
    con = sqlite3.connect(r"e:\classroom\python\dec10\library.db")
    cur = con.cursor()
    cur.execute("delete from books where id = ?", (id,))
    con.commit()
    con.close()
    return redirect("/demo/listbooks")
