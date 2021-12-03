# Generated by Django 3.2.7 on 2021-12-03 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_alter_order_instrument_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='instrument_type',
            field=models.CharField(choices=[('Simple Modification - Make from Scratch', 'Simple Modification - Make from Scratch'), ('Minor Mod to Standard Device', 'Minor Mod to Standard Device'), ('Complex Design - Requires Predicate', 'Complex Design - Requires Predicate'), ('Complex Assembly - Many Components', 'Complex Assembly - Many Components'), ('New Product', 'New Product')], help_text='Simple Modification - Make from Scratch: $750-1250\nMinor Mod to Standard Device: $1000-$2000\nComplex Design - Requires Predicate: $1750-$3000\nComplex Assembly - Many Components: $3000-$4500', max_length=39, null=True),
        ),
    ]