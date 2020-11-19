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
            'stock',
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
            'language': Select(attrs={'class': 'select2'})
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

    def clean(self): # aquí van las validaciones del formulario
        cleaned = super().clean() # aquí se recupera el objeto del formulario
        if not cleaned['ISBN'].isnumeric():
            self.add_error('ISBN', 'EL campo solo debe contener números')
            # raise forms.ValidationError('Error de algún tipo')
            # para presentar estos errores en el template se usa
            # {% for error in form.non_field_errors }
        # elif not cleaned['author'].isalpha():
        #    self.add_error('Autor', 'EL campo solo debe contener letras')
        #elif not cleaned['language'].isalpha():
        #    self.add_error('Lenguaje', 'EL campo solo debe contener letras')
        return cleaned