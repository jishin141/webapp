# Generated by Django 4.1.1 on 2022-11-15 05:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_rename_name_shipping_fullname'),
    ]

    operations = [
        migrations.CreateModel(
            name='payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('totalamount', models.CharField(max_length=255)),
                ('status', models.CharField(default='pending', max_length=255)),
                ('date', models.DateField()),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.register_form')),
            ],
        ),
    ]