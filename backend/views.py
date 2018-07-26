import json
import logging
import os
from django.http import HttpResponseForbidden, HttpResponseRedirect, JsonResponse, HttpResponse
from django.shortcuts import render, render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView
from cotAibc import settings
from backend.models import Books, Bookcases, Users, Orders
from backend.forms import BookEditForm

logger = logging.getLogger(__name__)


def index(request):
    return render_to_response('index.html')


class BaseMixin(object):
    def get_context_data(self, *args, **kwargs):
        context = super(BaseMixin, self).get_context_data(**kwargs)
        try:
            # 网站标题等内容
            context['website_title'] = settings.WEBSITE_TITLE
            context['website_welcome'] = settings.WEBSITE_WELCOME
        except Exception as e:
            logger.error(u'[BaseMixin]加载基本信息出错！')
        return context


class BooksView(BaseMixin, ListView):
    """
    Book query/edit/add.
    """
    template_name = 'books/index.html'
    context_object_name = 'book_list'
    paginate_by = settings.PAGE_NUM     # 分页--每页的数目

    def get_context_data(self, **kwargs):
        return super(BooksView, self).get_context_data(**kwargs)

    def get_queryset(self):
        book_list = Books.objects.filter(state=1)
        # for book in book_list:
        #     print(book, type(book))
        #     print("==================>", book.icon.url)
        return book_list

    # @login_required
    @csrf_exempt
    def new(request):
        if request.method == 'POST':
            form = BookEditForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/backend/books/')
        else:
            form = BookEditForm()
        return render( request, 'books/new.html', {'form': form, } )

    # @login_required
    @csrf_exempt
    def edit(request, book_id=0):
        book = Books.objects.get(book_id=book_id)
        if not book:
            logger.error(u'[Book]未找到记录！')

        if request.method == 'POST':
            form = BookEditForm(request.POST, request.FILES, instance=book)
            print('icon=========', request.FILES.get('icon'))
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/backend/books/')
        else:
            form = BookEditForm(instance=book)
        return render_to_response('books/edit.html', {'form': form, } )


class BookcasesView(BaseMixin, ListView):
    """
    Bookcases query/edit/add.
    """
    template_name = 'bookcases/index.html'
    context_object_name = 'bookcase_list'

    def get_context_data(self, **kwargs):
        return super(BookcasesView, self).get_context_data(**kwargs)

    def get_queryset(self):
        bookcase_list = Bookcases.objects.filter(state=1)
        return bookcase_list



class UsersView(BaseMixin, ListView):
    """
    Users query/edit/add.
    """
    template_name = 'users/index.html'
    context_object_name = 'user_list'

    def get_context_data(self, **kwargs):
        return super(UsersView, self).get_context_data(**kwargs)

    def get_queryset(self):
        user_list = Users.objects.filter(state=1)
        return user_list


class OrdersView(BaseMixin, ListView):
    """
    Orders query/edit/add.
    """
    template_name = 'orders/index.html'
    context_object_name = 'order_list'

    def get_context_data(self, **kwargs):
        return super(OrdersView, self).get_context_data(**kwargs)

    def get_queryset(self):
        order_list = Orders.objects.filter(state=1)
        return order_list



