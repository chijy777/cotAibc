import json
import logging
import os
import uuid

from django.core.files.base import ContentFile
from django.utils.datetime_safe import datetime
from django.core.files.images import ImageFile
from django.http import HttpResponseForbidden, HttpResponseRedirect, JsonResponse, HttpResponse
from django.shortcuts import render, render_to_response
from django.urls import reverse
from django.views import View
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

        # print(request)
        # print(book, book.book_id, book.book_name, book_id)
        if request.method == 'POST':
            print('=====================================\n')

            # form = PictureForm(request.POST, request.FILES)
            # if form.is_valid():
            #     f = request.FILES["imagefile"]
            #     # des_origin_path 为你在服务器上保存原始图片的文件物理路径
            #     des_origin_f = open(des_origin_path, "ab")
            #     for chunk in f.chunks():
            #         des_origin_f.write(chunk)
            #     des_origin_f.close()

            form = BookEditForm(request.POST, request.FILES, instance=book)
            print(request)
            print('img=========', request.FILES.get('img'))
            print('icon=========', request.FILES.get('icon'))
            print('=========', request.FILES)
            # print('=========', form)

            if form.is_valid():
                f = request.FILES.get("icon")
                print('=========', request.FILES)
                # 读取上传的文件中的video项为二进制文件
                # file_content = ContentFile(request.FILES['video'].read())
                # ImageField的save方法，第一个参数是保存的文件名，第二个参数是ContentFile对象，里面的内容是要上传的图片、视频的二进制内容
                # mymodel.video.save(request.FILES['video'].name, file_content)

                # print(form.cleaned_data)

                # 上传图片
                # upload_file = request.FILES.get('icon')
                # print(upload_file)
                # file_name_last = upload_file.name.split('.').pop()
                # file_name = 'IMG_{}.{}'.format(datetime.now().strftime('%Y%M%d%H%M%S'), file_name_last)
                # print(file_name)
                # with open(settings.MEDIA_ROOT + '/img/' + file_name, 'wb') as file:
                #     for chunk in upload_file.chunks():
                #         file.write(chunk)

                form.save()
                return HttpResponseRedirect('/backend/books/')
        else:
            form = BookEditForm(instance=book)
        return render_to_response('books/edit.html', {'form': form, } )

    # def upload_img(request):
    #     print('hahahahaha.')
    #     print(request)
    #     file = request.FILES.get('icon')
    #     path = os.path.join(settings.UPLOAD_ROOT, 'books', file.name)
    #     with open(path, 'w') as f:
    #         for p in f.chunks():
    #             f.write(p)
    #
    #     return JsonResponse({'code':'200', 'info':'upload ok!'})


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



# def uploadify_script(request):
#     ret = "0"
#     print('hhhhhha')
#     file = request.FILES.get("Filedata", None)
#     print(file)
#     if file:
#         result, new_name = profile_upload(file)
#         if result:
#             ret = "1"
#         else:
#             ret = "2"
#         jsonData = {'ret': ret, 'save_name': new_name}
#         return HttpResponse(
#             json.dumps(jsonData, ensure_ascii=False)
#         )
#
#
# def profile_upload(file):
#     '''文件上传函数'''
#     if file:
#         print(file.name)
#         path = os.path.join(settings.UPLOAD_ROOT, 'books')
#         # file_name=str(uuid.uuid1())+".jpg"
#         file_name = str(uuid.uuid1()) + '-' + file.name
#         # fname = os.path.join(settings.MEDIA_ROOT,filename)
#         path_file = os.path.join(path, file_name)
#         fp = open(path_file, 'wb')
#         for content in file.chunks():
#             fp.write(content)
#         fp.close()
#         return (True, file_name)  # change
#     return (False, file.name)  # change
#
#
# # 用户管理-添加用户-删除附件
# def profile_delte(request):
#     del_file = request.POST.get("delete_file", '')
#     if del_file:
#         path_file = os.path.join(settings.UPLOAD_ROOT, 'upload', del_file)
#         os.remove(path_file)


# @csrf_exempt
# def uploadify_script(request):
#     print('hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh')
#     response=HttpResponse()
#     response['Content-Type']="text/javascript"
#     ret="0"
#     file = request.FILES.get("Filedata",None)
#     if file:
#         if _upload(file):
#             ret="1"
#         ret="2"
#     response.write(ret)
#     return response
#
# def _upload(file):
#     '''''图片上传函数'''
#     if file:
#         path=os.path.join(settings.UPLOAD_ROOT,'upload')
#         file_name=str(uuid.uuid1())+".jpg"
#         path_file=os.path.join(path,file_name)
#         parser = ImageFile.Parser()
#         for chunk in file.chunks():
#             parser.feed(chunk)
#         img = parser.close()
#         try:
#             if img.mode != "RGB":
#                 img = img.convert("RGB")
#             img.save(path_file, 'jpeg',quality=100)
#         except:
#             return False
#         return True
#     return False
#
# def uploadImg(request): # 图片上传函数
#     # if request.method == 'POST':
#         # img = Image( img_url=request.FILES.get('img') )
#         # img.save()
#     return render(request, 'imgupload.html')


class UploadFile(View):
    def post(request):
        if request.method == 'POST':
            upload_file = request.FILES.get('icon')
            file_name_last = upload_file.name.split('.').pop()
            file_name = 'IMG_{}.{}'.format(datetime.now().strftime('%Y%M%d%H%M%S'), file_name_last)
            print(file_name)
            with open(settings.MEDIA_ROOT + '/img/' + file_name, 'wb') as file:
                for chunk in upload_file.chunks():
                    file.write(chunk)
        return HttpResponse("ok")
        # return render(request, 'success.html')


