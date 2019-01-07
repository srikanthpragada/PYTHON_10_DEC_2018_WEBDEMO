from django.urls import path
from . import views

urlpatterns = [
    path("welcome/", views.welcome),
    path("countries/", views.countries),
    path("countryinfo/", views.country_info),
]
