# Generated by Django 3.2.7 on 2021-12-01 07:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20211118_2141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='department',
        ),
    ]
