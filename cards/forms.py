from django.forms import ModelForm, TextInput
from .models import *


class DebitCardForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['number'].widget.attrs['autofocus'] = True

    class Meta:
        model = DebitCard
        fields = [
            'number',
            'nameInCard',
        ]
        widgets = {
            'number': TextInput(attrs={
                'placeholder': '1234-5678-9012-3456',
                'style': 'width: 50%',
                'class': 'form-control'}),
            'nameInCard': TextInput(attrs={
                'placeholder': 'Nombre en tarjeta',
                'style': 'width: 50%',
                'class': 'form-control'}),
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

    def clean(self):
        cleaned = super().clean()
        if not cleaned['number'].isnumeric():
            self.add_error('number', 'EL campo solo debe contener números')
        elif not cleaned['nameInCard'].replace(' ', '').isalpha():
            self.add_error('nameInCard', 'EL campo solo debe contener letras')
        return cleaned
