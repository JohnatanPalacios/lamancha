# Generated by Django 3.1.2 on 2020-11-28 02:09

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShippingDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipping_company', models.CharField(max_length=30)),
                ('guide_number', models.CharField(max_length=30)),
                ('shipping_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=1)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.book')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateField(default=datetime.datetime.now, verbose_name='Fecha de creación')),
                ('subtotal', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('complete', models.BooleanField(default=True, verbose_name='Estado de la compra')),
                ('details', models.ManyToManyField(to='orders.OrderDetails', verbose_name='Detalles del pedido')),
                ('shipping', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.shippingdetails', verbose_name='Envío')),
            ],
            options={
                'verbose_name': 'Pedido',
                'verbose_name_plural': 'Pedidos',
                'ordering': ['creation_date'],
            },
        ),
    ]
