# Generated by Django 3.2.19 on 2023-06-04 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='price_fabric',
            new_name='price',
        ),
    ]
