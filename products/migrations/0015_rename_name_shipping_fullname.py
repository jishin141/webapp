# Generated by Django 4.1.1 on 2022-11-15 04:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_alter_cart_tb_quantity_shipping'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shipping',
            old_name='name',
            new_name='fullname',
        ),
    ]
