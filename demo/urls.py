from django.urls import path
from . import views, book_views

urlpatterns = [
    path("welcome/", views.welcome),
    path("countries/", views.countries),
    path("countryinfo/", views.country_info),
    path("listbooks/", book_views.list_books),
    path("addbook/", book_views.add_book),
    path("deletebook/", book_views.delete_book),
]
