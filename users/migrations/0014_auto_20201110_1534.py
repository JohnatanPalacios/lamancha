# Generated by Django 3.1.2 on 2020-11-10 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20201110_1332'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='creditcard',
            name='id_customer',
        ),
        migrations.RemoveField(
            model_name='debitcard',
            name='id_customer',
        ),
        migrations.AddField(
            model_name='user',
            name='creditCards',
            field=models.ManyToManyField(to='users.CreditCard', verbose_name='Tarjetas de crédito'),
        ),
        migrations.AddField(
            model_name='user',
            name='debitCards',
            field=models.ManyToManyField(to='users.DebitCard', verbose_name='Tarjetas de débito'),
        ),
    ]