# Generated by Django 3.2.23 on 2024-02-23 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faqs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='question',
            field=models.CharField(default='', max_length=254),
            preserve_default=False,
        ),
    ]
