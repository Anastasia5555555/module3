# Generated by Django 4.2.5 on 2023-10-23 01:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_advertisement', '0015_advertisement_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advertisement',
            name='image',
        ),
        migrations.RemoveField(
            model_name='advertisement',
            name='user',
        ),
    ]
