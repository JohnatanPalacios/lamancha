# Generated by Django 3.1.2 on 2020-11-04 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20201103_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='birthday',
            field=models.CharField(max_length=12, verbose_name='Fecha de nacimiento'),
        ),
    ]