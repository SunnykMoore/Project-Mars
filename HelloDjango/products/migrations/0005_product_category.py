# Generated by Django 3.2.7 on 2021-10-07 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20211005_2100'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.TextField(default=''),
        ),
    ]
