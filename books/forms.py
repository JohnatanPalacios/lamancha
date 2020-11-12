from django.forms import *
from .models import Book
from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'


class BookForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for form in self.visible_fields():
        #   form.field.widget.attrs['class'] = 'form-control'
        self.fields['title'].widget.attrs['autofocus'] = True

    class Meta:
        model = Book
        fields = [
            'cover',
            'title',
            'author',
            'ISBN',
            'pages',
            'editorial',
            'price',
            'category',
            'language',
            'condition',
            'binding',
            'sale',
            'published_date',
            'description',
        ]
        widgets = {
            'cover': FileInput(),
            'title': TextInput(attrs={'placeholder': 'Lo Que Vi'}),
            'ISBN': TextInput(attrs={'placeholder': '9700517918'}),
            'published_date': DateInput(),
            'description': Textarea(),
        }