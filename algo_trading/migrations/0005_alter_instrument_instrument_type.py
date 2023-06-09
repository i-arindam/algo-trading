# Generated by Django 4.1.5 on 2023-03-31 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('algo_trading', '0004_alter_instrument_first_open_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instrument',
            name='instrument_type',
            field=models.CharField(choices=[('EQ', 'Equity'), ('FT', 'Futures'), ('OT', 'Options'), ('IX', 'Index'), ('CU', 'Currency'), ('CF', 'Currency Futures'), ('CO', 'Currency Options'), ('IF', 'Index Futures'), ('IO', 'Index Options')], default='EQ', max_length=2),
        ),
    ]
