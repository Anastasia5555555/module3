# Generated by Django 4.2.5 on 2023-10-22 03:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_advertisement', '0010_advertisement_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advertisement',
            name='user',
        ),
    ]
