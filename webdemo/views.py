# Function views

from django.http import HttpResponse
from datetime import datetime


def hello(request):
    return HttpResponse('<h1>Hello Django</h1>')


def wish(request):
    if 'name' in request.GET:
        name = request.GET["name"]  # Take value of name parameter
    else:
        name = "Unknown"

    cdt = datetime.now()
    if cdt.hour < 12:
        msg = "Good Morning"
    elif cdt.hour < 17:
        msg = "Good Afternoon"
    else:
        msg = "Good Evening"
    return HttpResponse(f'<h1>{msg} {name}</h1>')
