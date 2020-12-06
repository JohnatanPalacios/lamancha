# Generated by Django 3.1.2 on 2020-11-30 19:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_chat', models.CharField(blank=True, max_length=50, null=True, unique=True, verbose_name='id_chat')),
                ('contenido', models.CharField(max_length=100, verbose_name='contenido_mensaje')),
                ('hora_fecha', models.DateField(blank=True, null=True, verbose_name='Fecha de nacimiento')),
                ('estado', models.BooleanField(default=False)),
                ('id_emisor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Amigo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni_amigo', models.CharField(blank=True, max_length=50, null=True, unique=True, verbose_name='dni_chat')),
                ('nombre_amigo', models.CharField(max_length=50, verbose_name='nombre_amigo')),
                ('MENSAJE', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.mensaje')),
            ],
        ),
    ]
