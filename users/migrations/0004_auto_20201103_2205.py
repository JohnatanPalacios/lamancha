# Generated by Django 3.1.2 on 2020-11-04 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20201103_2145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='user_administrator',
        ),
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Dirección'),
        ),
    ]