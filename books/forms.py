from django.forms import *

from .models import Book


class BookRegistrationForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
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
            'description',
            'language',
            'condition',
            'binding',
            'category',
            'sale',
            'published_date',
            'price',
        ] # otra forma es _all_
        # otra forma de hacer los labels es usando el verbose_name
        # tambien es posible hacer esto con el field.label o form.name.label
        labels = {
            'username': 'Nombre de usuario'
        }
        # los widgets son las propiedades que tendrán los campos
        # es la forma de agregar el boostrap
        widgets = {
            'title': TextInput(
                attrs={
                    'placeholder': 'manchita',
                }
            ),
            'ISBN': TextInput(
                attrs={
                    'placeholder': 'La mancha'
                }
            ),
            'published_date': DateInput(),
        }