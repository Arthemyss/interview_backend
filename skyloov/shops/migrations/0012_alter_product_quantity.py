# Generated by Django 3.2.19 on 2023-06-06 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0011_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.PositiveIntegerField(default=1, verbose_name='quantity'),
        ),
    ]