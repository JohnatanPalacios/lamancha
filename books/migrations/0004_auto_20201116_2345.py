# Generated by Django 3.1.2 on 2020-11-17 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20201116_2344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='stock',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Cantidad en inventario'),
        ),
    ]
