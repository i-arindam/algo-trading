# Generated by Django 4.1.5 on 2023-04-04 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('algo_trading', '0009_alter_instrument_zerodha_instrument_token'),
    ]

    operations = [
        migrations.AlterOrderWithRespectTo(
            name='ohlcvdatadaily',
            order_with_respect_to='instrument_id',
        ),
    ]
