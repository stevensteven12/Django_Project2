# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-06-05 01:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('echo_example', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbindextable',
            name='TickTime',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='tbindextable',
            name='TradeDate',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='tbtraderecord',
            name='TickTime',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='tbtraderecord',
            name='TradeDate',
            field=models.CharField(max_length=20),
        ),
    ]
