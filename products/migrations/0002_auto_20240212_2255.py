# Generated by Django 3.2.23 on 2024-02-12 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='year',
            field=models.IntegerField(blank=True, null=True, verbose_name='Year'),
        ),
        migrations.DeleteModel(
            name='Year',
        ),
    ]
