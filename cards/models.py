from django.db import models


class CreditCard(models.Model):
    number = models.CharField(max_length=20, verbose_name='Número de la Tarjeta', blank=False, null=False)
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
    number = models.CharField(max_length=20, verbose_name='Número de la Tarjeta', blank=False, null=False)
    nameInCard = models.CharField(max_length=150, verbose_name='Nombre en Tarjeta', blank=False, null=False)

    def __str__(self):
        return 'Tarjeta Número: {}'.format(self.number)

    class Meta:
        verbose_name = 'Tarjeta Débito'
        verbose_name_plural = 'Tarjetas Débito'
        ordering = ['id']
