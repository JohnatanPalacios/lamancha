# Generated by Django 3.1.2 on 2020-12-10 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20201210_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensaje',
            name='contenido',
            field=models.CharField(max_length=500, verbose_name='contenido_mensaje'),
        ),
    ]
