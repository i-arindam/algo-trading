# Generated by Django 4.1.5 on 2023-03-29 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('algo_trading', '0003_alter_instrument_first_open_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instrument',
            name='first_open_date',
            field=models.DateField(blank=True, default=None, null=True, verbose_name='instrument first traded date'),
        ),
    ]
