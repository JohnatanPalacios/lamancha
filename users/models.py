# Django
from django.contrib.auth.models import User
from django.db import models as m


class Customer(m.Model):
    user = m.OneToOneField(User, on_delete=m.CASCADE, related_name='customer')
    dni = m.CharField(max_length=50, verbose_name='DNI', unique=True, null=True, blank=True)
    photo = m.ImageField(upload_to='customer/photos', null=True, blank=True)
    address = m.CharField(max_length=150, verbose_name='Dirección', null=True, blank=True)
    birthday = m.CharField(max_length=12, verbose_name='Fecha de nacimiento', null=True, blank=True)
    gender = m.CharField(max_length=10, verbose_name='Género', null=True, blank=True)
    favoriteGenres = m.CharField(max_length=120, verbose_name='Preferencias Literarias', blank=True, null=True)
    news = m.BooleanField(default=True, null=True, blank=True)

    def __str__(self):
        return 'Nombre: {} / Apellido: {}'.format(self.user.first_name, self.user.last_name)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['dni']


class Card(m.Model):
    number = m.CharField(max_length=20, verbose_name='Número de la Tarjeta', blank=False, null=False)
    nameInCard = m.CharField(max_length=150, verbose_name='Nombre en Tarjeta', blank=False, null=False)
    month_expiration = m.CharField(max_length=2, verbose_name='Mes de expiración', blank=True, null=True)
    day_expiration = m.CharField(max_length=2, verbose_name='Día de Expiración', blank=True, null=True)
    id_customer = m.ForeignKey(Customer, on_delete=m.CASCADE, blank=False, null=False)

    def __str__(self):
        return 'Tarjeta Número: {}'.format(self.number)

    class Meta:
        verbose_name = 'Tarjeta'
        verbose_name_plural = 'Tarjetas'
        ordering = ['id']
