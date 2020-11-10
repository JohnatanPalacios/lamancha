# Django
from django.db import models as m

# Tools
from datetime import datetime


class Book(m.Model):
    ISBN = m.CharField(max_length=13, verbose_name='ISBN', blank=False, null=False)
    title = m.CharField(max_length=150, verbose_name='Título', blank=False, null=False)
    published_date = m.DateField(verbose_name='Fecha de publicación', blank=True, null=True)
    pages = m.CharField(max_length=50, verbose_name='Páginas', blank=True, null=True)
    price = m.DecimalField(default=0.00, max_digits=9, decimal_places=2, blank=False, null=False)
    cover = m.ImageField(upload_to='product/%Y/%m/%d', null=True, blank=True)
    description = m.TextField(verbose_name='Descripción', blank=True, null=True)
    sale = m.BooleanField(default=True, blank=False, null=False)
    condition = m.CharField(max_length=10, verbose_name='Condición', blank=True, null=True)
    editorial = m.CharField(max_length=50, verbose_name='Editorial', blank=True, null=True)
    language = m.CharField(max_length=50, verbose_name='Lenguaje', blank=False, null=False)
    author = m.CharField(max_length=50, verbose_name='Autor', blank=False, null=False)
    binding = m.CharField(max_length=15, verbose_name='Encuadernación', blank=True, null=True)
    category = m.CharField(max_length=50, verbose_name='Categoría', blank=True, null=True)
    # id_shoppingCart = m.ForeignKey(ShoppingCart, on_delete=m.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
        ordering = ['title']