# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2020-01-18 09:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message_routing', '0002_auto_20200118_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gateway',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='ipaddress',
            name='address',
            field=models.CharField(max_length=200),
        ),
    ]
