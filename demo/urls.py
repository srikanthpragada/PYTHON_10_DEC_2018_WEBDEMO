from django.urls import path
from . import views, book_views, orm_book_views

urlpatterns = [
    path("welcome/", views.welcome),
    path("countries/", views.countries),
    path("countryinfo/", views.country_info),
    path("listbooks/", book_views.list_books),
    path("addbook/", book_views.add_book),
    path("deletebook/", book_views.delete_book),
    path('add_cookie/', views.add_cookie ),
    path('list_cookies/', views.list_cookies),
    path('session_names/', views.session_names),
    # ORM related urls
    path("orm/listbooks/", orm_book_views.list_books),
    path("orm/addbook/", orm_book_views.add_book),
    path("orm/deletebook/", orm_book_views.delete_book),
    path("orm/searchbooks/", orm_book_views.search_books),
    path("orm/getbooks/", orm_book_views.get_books),
    path("orm/home/", orm_book_views.home_books),
    path("orm/summary/", orm_book_views.books_summary),
]
