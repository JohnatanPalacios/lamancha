# Generated by Django 3.1.2 on 2020-11-09 18:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20201109_0426'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Card',
            new_name='CreditCard',
        ),
        migrations.AlterModelOptions(
            name='creditcard',
            options={'ordering': ['id'], 'verbose_name': 'Tarjeta de Crédito', 'verbose_name_plural': 'Tarjetas de Crédito'},
        ),
        migrations.CreateModel(
            name='DebitCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=20, verbose_name='Número de la Tarjeta')),
                ('nameInCard', models.CharField(max_length=150, verbose_name='Nombre en Tarjeta')),
                ('id_customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Tarjeta Débito',
                'verbose_name_plural': 'Tarjetas Débito',
                'ordering': ['id'],
            },
        ),
    ]
