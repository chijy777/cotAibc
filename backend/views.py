import logging
from django.http import HttpResponseForbidden
from django.shortcuts import render, render_to_response
from django.views.generic import ListView
from cotAibc import settings
from backend.models import Books, Bookcases, Users, Orders
from backend.forms import BookEditForm

logger = logging.getLogger(__name__)


def index(request):
    return render_to_response('backend/index.html')

class BaseMixin(object):
    def get_context_data(self, *args, **kwargs):
        context = super(BaseMixin, self).get_context_data(**kwargs)
        try:
            # 网站标题等内容
            context['website_title'] = settings.WEBSITE_TITLE
            context['website_welcome'] = settings.WEBSITE_WELCOME
            # # 热门文章
            # context['hot_article_list'] = Article.objects.order_by("-view_times")[0:10]
            # # 导航条
            # context['nav_list'] = Nav.objects.filter(status=0)
            # # 最新评论
            # context['latest_comment_list'] = Comment.objects.order_by("-create_time")[0:10]
            # # 友情链接
            # context['links'] = Link.objects.order_by('create_time').all()
            # colors = ['primary', 'success', 'info', 'warning', 'danger']
            # for index, link in enumerate(context['links']):
            #     link.color = colors[index % len(colors)]
            # # 用户未读消息数
            # user = self.request.user
            # if user.is_authenticated():
            #     context['notification_count'] = user.to_user_notification_set.filter(is_read=0).count()
        except Exception as e:
            logger.error(u'[BaseMixin]加载基本信息出错！')
        return context



class BooksView(BaseMixin, ListView):
    """
    Book
    """
    template_name = 'backend/books/index.html'
    context_object_name = 'book_list'
    paginate_by = settings.PAGE_NUM     # 分页--每页的数目

    def get_context_data(self, **kwargs):
        # kwargs['carousel_page_list'] = Books.objects.all()
        return super(BooksView, self).get_context_data(**kwargs)

    def get_queryset(self):
        book_list = Books.objects.filter(state=1)
        return book_list

    # @login_required
    def new(request):
        if request.method == 'POST':
            form = BookEditForm(request.POST)
            if form.is_valid():
                print(form.cleaned_data)
                # book.save()
                return render(request, 'backend/books/index.html')
        else:
            form = BookEditForm()
        return render( request, 'backend/books/new.html', {'form': form, } )

    # @login_required
    def edit(request, book_id=0):
        print(request)
        book = Books.objects.get(book_id=book_id)
        if not book:
            logger.error(u'[Book]未找到记录！')
            # return HttpResponseForbidden(_('Editing is not allowed when topic has been replied'))
        print(book, book.book_id, book.book_name, book_id)
        if request.method == 'POST':
            form = BookEditForm(request.POST, instance=book)
            if form.is_valid():
                print(form.cleaned_data)
                # book.save()
                # return HttpResponseRedirect(
                #     reverse('niji:topic', kwargs={'bid': t.pk})
                # )
        else:
            form = BookEditForm(instance=book)
        return render( request, 'backend/books/edit.html', {'form': form, } )



class BookcasesView(BaseMixin, ListView):
    """
    Bookcases.
    """
    template_name = 'backend/bookcases/index.html'
    context_object_name = 'bookcase_list'

    def get_context_data(self, **kwargs):
        return super(BookcasesView, self).get_context_data(**kwargs)

    def get_queryset(self):
        bookcase_list = Bookcases.objects.filter(state=1)
        return bookcase_list



class UsersView(BaseMixin, ListView):
    """
    Users.
    """
    template_name = 'backend/users/index.html'
    context_object_name = 'user_list'

    def get_context_data(self, **kwargs):
        return super(UsersView, self).get_context_data(**kwargs)

    def get_queryset(self):
        user_list = Users.objects.filter(state=1)
        return user_list



class OrdersView(BaseMixin, ListView):
    """
    Orders.
    """
    template_name = 'backend/orders/index.html'
    context_object_name = 'order_list'

    def get_context_data(self, **kwargs):
        return super(OrdersView, self).get_context_data(**kwargs)

    def get_queryset(self):
        order_list = Orders.objects.filter(state=1)
        return order_list
