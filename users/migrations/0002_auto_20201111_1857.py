# Generated by Django 3.1.2 on 2020-11-11 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.ImageField(blank=True, default='static/images/default-profile.png', null=True, upload_to='customer/photos'),
        ),
    ]
