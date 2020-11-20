# Django
from django.db import models as m
from django.forms import model_to_dict

from lamancha.settings import MEDIA_URL, STATIC_URL


book_condition = [
    ('Nuevo', 'Nuevo'),
    ('Usado', 'Usado')
]


class Language(m.Model):
    language = m.CharField(max_length=20, verbose_name='Lenguaje')

    def __str__(self):
        return str(self.language)

    class Meta:
        verbose_name = 'Lenguaje'
        verbose_name_plural = 'Lenguajes'
        ordering = ['language']


class Book(m.Model):
    ISBN = m.CharField(max_length=13, verbose_name='ISBN', blank=False, null=False)
    title = m.CharField(max_length=150, verbose_name='Título', blank=False, null=False)
    published_date = m.DateField(verbose_name='Fecha de publicación', blank=True, null=True)
    pages = m.CharField(max_length=50, verbose_name='Páginas', blank=True, null=True)
    price = m.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Precio', blank=False, null=False)
    cover = m.ImageField(upload_to='product/%Y/%m/%d', default='static/images/default-book.png', verbose_name='Foto de portada', null=True, blank=True)
    description = m.TextField(verbose_name='Descripción', blank=True, null=True)
    sale = m.BooleanField(default=True, verbose_name='En venta', blank=False, null=False)
    condition = m.CharField(max_length=10, choices=book_condition, verbose_name='Condición', blank=True, null=True)
    editorial = m.CharField(max_length=50, verbose_name='Editorial', blank=True, null=True)
    language = m.ForeignKey(Language, on_delete=m.CASCADE, verbose_name='Idioma')
    author = m.CharField(max_length=50, verbose_name='Autor', blank=False, null=False)
    binding = m.CharField(max_length=15, verbose_name='Encuadernación', blank=True, null=True)
    category = m.CharField(max_length=50, verbose_name='Categoría', blank=True, null=True)
    stock = m.IntegerField(default=0, verbose_name='Cantidad en inventario', blank=True, null=True)

    # id_shoppingCart = m.ForeignKey(ShoppingCart, on_delete=m.CASCADE)

    def __str__(self):
        return str(self.title)

    def toJSON(self):
        item = model_to_dict(self, exclude=['cover'])
        item['title'] = self.title
        item['author'] = self.author
        item['cover'] = self.get_image()
        item['price'] = format(self.price, '.2f')
        return item

    def get_image(self):
        if self.cover:
            return '{}{}'.format(MEDIA_URL, self.cover)
        return '{}{}'.format(STATIC_URL, 'images/default-book.png')

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
        ordering = ['title']
