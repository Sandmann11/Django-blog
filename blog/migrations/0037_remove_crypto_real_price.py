# Generated by Django 3.1.7 on 2021-04-15 01:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0036_crypto_real_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crypto',
            name='real_price',
        ),
    ]
