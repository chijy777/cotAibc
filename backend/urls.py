from backend.views import index, BooksView, BookcasesView, UsersView, OrdersView, UploadFile
from django.conf import settings
from django.conf.urls import url
from django.template.context_processors import static
from django.urls import path
from django.views.generic import TemplateView, DetailView


urlpatterns = [
    url(r'^$', index, name='backend_index' ),

    url(r'^books/$', BooksView.as_view(), name='books_index'),
    url(r'^books/new/$', BooksView.new, name='books_new'),
    url(r'^books/edit/(?P<book_id>\d+)/$', BooksView.edit, name='books_edit'),
    # url(r'^books/upload/img/$', BooksView.upload_img, name='books_upload_img'),

    url(r'^bookcases/$', BookcasesView.as_view(), name='bookcases_index'),

    url(r'^users/$', UsersView.as_view(), name='users_index'),

    url(r'^orders/$', OrdersView.as_view(), name='orders_index'),

    # url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

    # url(r'^upload_script/$', uploadify_script, name='upload_script'),
    # # url(r'^delete_uploadfile/$', profile_delte, name='delete_uploadfile'),
    # url(r'^uploadImg/$', uploadImg), # 新增

    # url(r'upload/$', UploadFile.post),
    # url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

]

