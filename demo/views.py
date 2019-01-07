from django.shortcuts import render
import requests


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
        return render(request, 'countries.html', {'countries' : countries})


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
                      {'code': code, 'country' : country, 'message' : message})
    else:
        return render(request,'country_info.html')

