# Generated by Django 3.1.2 on 2020-11-09 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_user_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, choices=[(0, 'Femenino'), (1, 'Masculino'), (2, 'Otro')], max_length=9, null=True, verbose_name='Género'),
        ),
    ]
