# Generated by Django 3.2.23 on 2024-02-23 01:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20240221_0814'),
        ('newsletter', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Newsletter',
            new_name='Subscriber',
        ),
    ]
