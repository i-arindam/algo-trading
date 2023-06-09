# Generated by Django 4.1.5 on 2023-04-04 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('algo_trading', '0005_alter_instrument_instrument_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='instrument',
            options={'get_latest_by': 'id', 'verbose_name': 'Instrument', 'verbose_name_plural': 'Instruments'},
        ),
        migrations.AddIndex(
            model_name='instrument',
            index=models.Index(fields=['symbol'], name='instrument_symbol_idx'),
        ),
        migrations.AddIndex(
            model_name='instrument',
            index=models.Index(fields=['instrument_type'], name='instrument_instrument_type_idx'),
        ),
    ]
