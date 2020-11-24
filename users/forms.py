from django.contrib.auth import password_validation
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.forms import UserCreationForm
from django.forms import *
from .models import *
from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'


class UserRegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for form in self.visible_fields():
        #    form.fields.widget.attrs['class'] = 'form-control'
        #    form.fields.widget.attrs['autocomplete'] = 'off'
        self.fields['username'].widget.attrs['autofocus'] = True
        # self.fields['password1'].required = False
        password1 = forms.CharField(label=_('Password'),
                                    widget=(forms.PasswordInput(attrs={'class': 'form-control'})),
                                    help_text=password_validation.password_validators_help_text_html())
        password2 = forms.CharField(label=_('Password Confirmation'),
                                    widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                                    help_text=_('Just Enter the same password, for confirmation'))

    class Meta:
        model = User
        fields = [
            'photo',
            'username',
            'first_name',
            'last_name',
            'dni',
            'email',
            'birthday',
            'gender',
            'password1',
            'password2',
            'address',
            'favoriteGenres',
            'news'
        ]
        labels = {
            'username': 'Nombre de usuario',
            'first_name': 'Nombres',
            'last_name': 'Apellidos',
            'birthday': 'Fecha de nacimiento',
            'gender': 'Género',
            'news': 'Recibir Noticias',
            'email': 'Correo electrónico',
            'address': 'Dirección de correspondencia',
            'dni': 'Documento de identificación',
            'favoriteGenres': 'Géneros literarios de preferencia',
        }
        widgets = {
            'photo': FileInput(),
            'username': TextInput(attrs={
                'placeholder': 'manchita',
            }),
            'dni': TextInput(attrs={
                'placeholder': '123456789',
            }),
            'first_name': TextInput(attrs={
                'placeholder': 'La mancha'
            }),
            'password1': PasswordInput(attrs={
                'placeholder': 'Contraseña',
                'autocomplete': 'off',
            }),
            'password2': PasswordInput(attrs={
                'placeholder': 'Confirma la contraseña',
                'autocomplete': 'off',
            }),
            'email': EmailInput(attrs={
                'placeholder': 'user@lamancha.com',
            }),
            'news': CheckboxInput(),
            'birthday': DateInput(),
            'gender': Select(attrs={
                'class': 'select2 js-example-responsive',
                'style': 'width: 65%',
                'language': 'es',
                'theme': 'bootstrap4',
            }),
            'favoriteGenres': SelectMultiple(attrs={
                'class': 'select2 js-example-responsive',
                'style': 'width: 100%',
                # 'multiple': 'multiple',
                'multiple': True,
                'language': 'es',
                'theme': 'bootstrap4',
                'placeholder': 'Seleccione sus preferencias literarias..'
            }),
            'address': TextInput(attrs={
                'placeholder': 'Mirador de Pinares T2 Ap1109',
            })
        }
        exclude = ['groups', 'user_permissions', 'last_login', 'date_joined', 'is_staff', 'is_superuser', 'is_active']

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                user = form.save(commit=False)
                form.save()
                for favoriteGenre in self.cleaned_data['favoriteGenres']:
                    user.favoriteGenres.add(favoriteGenre)
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


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
