# Generated by Django 3.2.23 on 2024-02-23 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20240221_0814'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sold',
            field=models.BooleanField(default=False),
        ),
    ]