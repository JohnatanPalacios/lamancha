# Generated by Django 3.1.2 on 2020-11-09 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20201109_0416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, max_length=9, null=True, verbose_name='Género'),
        ),
    ]
