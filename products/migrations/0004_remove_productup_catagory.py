# Generated by Django 4.1.1 on 2022-10-27 04:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_productup_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productup',
            name='catagory',
        ),
    ]