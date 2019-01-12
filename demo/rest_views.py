from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from demo.models import Book
from demo.serializers import BookSerializer


def rest_client(request):
    return render(request, 'rest_client.html')


@api_view(['GET', 'POST'])
def book_process(request):
    if request.method == "GET":
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    else:  # POST
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # insert into table
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)  # bad request


@api_view(['GET', 'DELETE'])
def one_book_process(request, id):
    try:
        book = Book.objects.get(id=id)
    except:
        return Response(status=404)  # Send 404 to client

    if request.method == "GET":
        serializer = BookSerializer(book)
        return Response(serializer.data)
    else:  # Delete
        book.delete()
        return Response(status=204)  # No data
