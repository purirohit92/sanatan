# Generated by Django 3.2.2 on 2022-04-23 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0027_cart_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='price_ht',
        ),
    ]
