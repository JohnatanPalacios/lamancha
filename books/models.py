from django.db import models as m

class Book(m.Model):
    ISBN = m.CharField(max_length=150, verbose_name='ISBN', blank=False, null=False)
    title = m.CharField(max_length=150, verbose_name='Título', blank=False, null=False)
    published_date = m.DateTimeField(default=datetime.now,
                                     verbose_name='Fecha de publicación',
                                     blank=False,
                                     null=False)
    pages = m.CharField(max_length=50, verbose_name='Páginas', blank=False, null=False)
    price = m.DecimalField(default=0.00, max_digits=9, decimal_places=2, blank=False, null=False)
    image = m.ImageField(upload_to='product/%Y/%m/%d', null=True, blank=True)
    description = m.TextField(verbose_name='Descripción', blank=False, null=False)
    sale = m.BooleanField(default=True, blank=False, null=False)
    id_condition = m.ForeignKey(Condition, related_name='conditions', on_delete=m.CASCADE, blank=False, null=False)
    id_editorial = m.ForeignKey(Editorial, related_name='editorials', on_delete=m.CASCADE, blank=False, null=False)
    id_language = m.ForeignKey(Language, related_name='languages', on_delete=m.CASCADE, blank=False, null=False)
    authors = m.ManyToManyField(Author, related_name='books')
    id_shoppingCart = m.ForeignKey(ShoppingCart, on_delete=m.CASCADE)

    def __str__(self):
        return 'Título: {} / ISBN: {}'.format(self.title, self.ISBN)

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
        ordering = ['title']