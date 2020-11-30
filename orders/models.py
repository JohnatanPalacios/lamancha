from django.db import models as m
from django.forms import model_to_dict
from lamancha.settings import MEDIA_URL, STATIC_URL
from books.models import Book
from users.models import User
from datetime import datetime


class OrderDetails(m.Model):
    book = m.ForeignKey(Book, on_delete=m.CASCADE, blank=False, null=False)
    amount = m.IntegerField(default=1, blank=False, null=False)

    def __str__(self):
        total = self.book.price * self.amount
        return str(total)


class ShippingDetails(m.Model):
    shipping_company = m.CharField(max_length=30)
    guide_number = m.CharField(max_length=30)
    shipping_date = m.DateField()

    def __str__(self):
        return 'Guía N°: {}'.format(self.guide_number)


class Order(m.Model):
    user = m.ForeignKey(User, on_delete=m.CASCADE, blank=False, null=False)
    creation_date = m.DateField(default=datetime.now, verbose_name='Fecha de creación', blank=False, null=False)
    details = m.ManyToManyField(OrderDetails, verbose_name= 'Detalles del pedido', blank=False)
    shipping = m.ForeignKey(ShippingDetails, verbose_name='Envío', on_delete=m.CASCADE)
    subtotal = m.DecimalField(default=0.00, max_digits=9, decimal_places=2, blank=False, null=False)
    total = m.DecimalField(default=0.00, max_digits=9, decimal_places=2, blank=False, null=False)
    complete = m.BooleanField(default=True, verbose_name='Estado de la compra', blank=False, null=False)

    def __str__(self):
        return str(self.creation_date)

    def toJSON(self):
        item = model_to_dict(self)
        item['subtotal'] = format(self.subtotal, '.2f')
        item['total'] = format(self.total, '.2f')
        return item

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        ordering = ['creation_date']

