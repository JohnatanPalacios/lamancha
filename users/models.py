# Django
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.forms import model_to_dict
from lamancha.settings import MEDIA_URL, STATIC_URL

GENDERS = [
    ('Femenino', 'Femenino'),
    ('Masculino', 'Masculino'),
    ('Otro', 'Otro')
]



class LiteraryGenders(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Género literario'
        verbose_name_plural = 'Géneros literarios'
        ordering = ['name']

    def __str__(self):
        return self.name


class CreditCard(models.Model):
    number = models.CharField(max_length=20, unique=True, verbose_name='Número de la Tarjeta', blank=False, null=False)
    nameInCard = models.CharField(max_length=150, verbose_name='Nombre en Tarjeta', blank=False, null=False)
    month_expiration = models.CharField(max_length=2, verbose_name='Mes de expiración', blank=True, null=True)
    day_expiration = models.CharField(max_length=2, verbose_name='Día de Expiración', blank=True, null=True)

    def __str__(self):
        return 'Tarjeta Número: {}'.format(self.number)

    class Meta:
        verbose_name = 'Tarjeta de Crédito'
        verbose_name_plural = 'Tarjetas de Crédito'
        ordering = ['id']


class DebitCard(models.Model):
    number = models.CharField(max_length=20, unique=True, verbose_name='Número de la Tarjeta', blank=False, null=False)
    nameInCard = models.CharField(max_length=150, verbose_name='Nombre en Tarjeta', blank=False, null=False)

    def __str__(self):
        return 'Tarjeta Número: {}'.format(self.number)

    def toJSON(self):
        item = model_to_dict(self)
        item['icon'] = self.get_icon()
        item['number'] = self.last_digits()
        return item

    def get_icon(self):
        return '{}{}'.format(STATIC_URL, 'images/icons/pay-visa.png')

    def last_digits(self):
        digits = ''
        for i in range((len(self.number) - 4), len(self.number)):
            digits += self.number[i]
        return digits

    class Meta:
        verbose_name = 'Tarjeta Débito'
        verbose_name_plural = 'Tarjetas Débito'
        ordering = ['id']



class User(AbstractUser):
    dni = models.CharField(max_length=50, verbose_name='DNI', unique=True, null=True, blank=True)
    photo = models.ImageField(upload_to='customer/photos', default='static/images/default-profile.png', null=True,
                              blank=True)
    address = models.CharField(max_length=150, verbose_name='Dirección', null=True, blank=True)
    birthday = models.DateField(verbose_name='Fecha de nacimiento', null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDERS, verbose_name='Género', null=True, blank=True)
    favoriteGenres = models.ManyToManyField(LiteraryGenders, verbose_name='Preferencias literarias', blank=True)
    news = models.BooleanField(default=True, null=True, blank=True)
    email = models.EmailField(_('email address'), unique=True, null=False, blank=False)
    debitCards = models.ManyToManyField(DebitCard, verbose_name='Tarjetas de débito')
    creditCards = models.ManyToManyField(CreditCard, verbose_name='Tarjetas de crédito')
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']
    def __str__(self):
        return str(self.username)

    def get_photo(self):
        if self.photo:
            return '{}{}'.format(MEDIA_URL, self.photo)
        return '{}{}'.format(STATIC_URL, 'images/default-profile.png')

    def toJSON(self):
        item = model_to_dict(self, exclude=['password', 'groups', 'user_permissions', 'last_login'])
        if self.last_login:
            item['last_login'] = self.last_login.strftime('%Y-%m-%d')
        item['date_joined'] = self.date_joined.strftime('%Y-%m-%d')
        item['photo'] = self.get_photo()
        item['full_name'] = self.get_full_name()
        return item

    def save(self, *args, **kwargs):
        if self.pk is None:
            # self.set_password(self.password)
            self.password = self.password
        else:
            user = User.objects.get(pk=self.pk)
            if user.password != self.password:
                user.password = self.password
        super().save(*args, **kwargs)

class Mensaje(models.Model):
    """docstring for mensaje"""
    id_chat = models.CharField(max_length=50, verbose_name='id_chat', unique=True, null=True, blank=True)
    contenido = models.CharField(max_length=100, verbose_name='contenido_mensaje')
    hora_fecha = models.DateField(verbose_name='Fecha de envio', null=True, blank=True)
    id_emisor = models.ForeignKey(User, on_delete=models.CASCADE)
    id_receptor = models.CharField(max_length=50, verbose_name='id_receptor', unique=True, null=True, blank=True)
    estado = models.BooleanField(default=False)
    def __str__(self):
        return str(self.id_chat + self.contenido)

    class Meta:
        verbose_name = "Mensaje"
        verbose_name_plural = "Mensajes"
        ordering = ["hora_fecha"]

