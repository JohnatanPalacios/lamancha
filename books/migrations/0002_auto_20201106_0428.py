# Generated by Django 3.1.2 on 2020-11-06 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='image',
            new_name='cover',
        ),
    ]