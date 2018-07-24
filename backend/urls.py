from backend.views import index, BooksView, BookcasesView, UsersView, OrdersView
from django.conf.urls import url
from django.urls import path
from django.views.generic import TemplateView, DetailView


urlpatterns = [
    url(r'^$', index, name='backend_index' ),

    path('books/', BooksView.as_view(), name='books_index'),
    path('books/new/', BooksView.new, name='books_new'),
    path('books/edit/(?P<book_id>\d+)/', BooksView.edit, name='books_edit'),

    path(r'bookcases/', BookcasesView.as_view(), name='bookcases_index'),

    path(r'users/', UsersView.as_view(), name='users_index'),

    path(r'orders/', OrdersView.as_view(), name='orders_index'),
]
