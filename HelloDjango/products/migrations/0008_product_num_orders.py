# Generated by Django 3.2.7 on 2021-11-18 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20211007_2107'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='num_orders',
            field=models.PositiveIntegerField(default=0),
        ),
    ]