from backend.models import Books
from django import forms

class BookEditForm(forms.ModelForm):
    """
    Books
    """
    def __init__(self, *args, **kwargs):
        super(BookEditForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Books
        fields = (
            'book_id', 'book_name', 'author', 'icon', 'press', 'pub_date',
            'pages', 'prices', 'isdn', 'brief', 'scores', 'douban_url',
        )

