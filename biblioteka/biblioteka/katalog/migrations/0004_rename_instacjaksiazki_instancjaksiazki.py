# Generated by Django 4.2.1 on 2023-05-26 11:57

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('katalog', '0003_ksiazka_gatunek'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='InstacjaKsiazki',
            new_name='InstancjaKsiazki',
        ),
    ]
