# Generated by Django 4.1.5 on 2023-04-11 06:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('algo_trading', '0011_alter_ohlcvdatadaily_order_with_respect_to'),
    ]

    operations = [
        migrations.DeleteModel(
            name='OhlcvDataDaily',
        ),
    ]
