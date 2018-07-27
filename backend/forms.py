from backend.models import Books
from django import forms
from django.forms import ClearableFileInput


class BookEditForm(forms.ModelForm):
    """
    Books
    """
    def __init__(self, *args, **kwargs):
        super(BookEditForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Books
        fields = (
            'book_id', 'book_name', 'author',
            'icon', 'press', 'pub_date',
            'pages', 'prices', 'isdn',
            'brief', 'scores', 'douban_url',
        )
        # widgets = {'backend_image': ImageWidget}


class ImageWidget(ClearableFileInput):
    template_with_initial = (
        '%(initial_text)s: <a href="%(initial_url)s"><img width="100px" height="100px" src="%(initial_url)s"></a> '
        '%(clear_template)s<br />%(input_text)s: %(input)s'
    )
    template_with_clear = ''
