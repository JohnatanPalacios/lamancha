from django.contrib.auth import password_validation
from django.utils.translation import gettext_lazy as _


from django.contrib.auth.forms import UserCreationForm
from django.forms import *
from users.models import User
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
            'favoriteGenres': 'Géneros literarios de preferencia',
        }
        # los widgets son las propiedades que tendrán los campos
        # es la forma de agregar el boostrap
        widgets = {
            'photo': FileInput(),
            'username': TextInput(attrs={
                'placeholder': 'manchita',
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
            'gender': Select(),
            'favoriteGenres': SelectMultiple(attrs={
                'class': 'form-control select2',
                'style': 'width: 100%',
                'multiple': 'multiple'
            })
        }
        exclude = ['groups', 'user_permissions', 'last_login', 'date_joined', 'is_staff', 'is_superuser', 'is_active']

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

