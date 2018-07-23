from backend.views import index, BooksView, BookcasesView, UsersView, OrdersView
from django.conf.urls import url
from django.views.generic import TemplateView, DetailView


urlpatterns = [
    url(r'^$', index ),

    url(r'^books$', BooksView.as_view(), name='books_index'),
    url(r'^books/new/$', BooksView.new, name='books_new'),
    url(r'^books/edit/(?P<book_id>\d+)/$', BooksView.edit, name='books_edit'),

    url(r'^bookcases$', BookcasesView.as_view(), name='bookcases_index'),

    url(r'^users$', UsersView.as_view(), name='users_index'),

    url(r'^orders$', OrdersView.as_view(), name='orders_index'),
]

