from django.shortcuts import render
from django.http import HttpResponseRedirect
import requests
import datetime


# Create your views here.

def welcome(request):
    return render(request, 'welcome.html')


def countries(request):
    resp = requests.get("https://restcountries.eu/rest/v2/all")
    if resp.status_code != 200:
        message = "Sorry! Could not get details of countries!"
        return render(request, 'countries.html', {'message': message})
    else:
        countries = resp.json()
        return render(request, 'countries.html', {'countries': countries})


def country_info(request):
    if 'code' in request.POST:
        code = request.POST['code']
        resp = requests.get(f"https://restcountries.eu/rest/v2/alpha/{code}")
        message = None
        country = None
        if resp.status_code != 200:
            message = "Sorry! Could not get details of country!"
        else:
            country = resp.json()

        return render(request, 'country_info.html',
                      {'code': code, 'country': country, 'message': message})
    else:
        return render(request, 'country_info.html')


def add_cookie(request):
    if request.method == "GET":
        return render(request, 'add_cookie.html')
    else:  # POST
        # process data
        name = request.POST["cookie_name"]
        value = request.POST["cookie_value"]
        response = HttpResponseRedirect("/demo/list_cookies/")
        if 'durable' in request.POST:  # is checkbox selected
            # Create a durable cookie
            response.set_cookie(name, value, expires=datetime.datetime.now() + datetime.timedelta(days=10))
        else:
            # Create a browser-based cookie
            response.set_cookie(name, value)

    return response


def list_cookies(request):
    return render(request, 'list_cookies.html', {'cookies': request.COOKIES})


def session_names(request):
    # either take existing names or empty list
    if 'names' in request.session:
        names = request.session['names']
    else:
        names = []

    if request.method == "POST":
        # add name to list
        fullname = request.POST["fullname"]
        names.append(fullname)
        request.session['names'] = names

    return render(request, 'session_names.html', {'names': names})
