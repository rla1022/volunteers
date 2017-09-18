# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-12 19:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hours', '0004_hourslocation_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='hourslocation',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='hourslocation',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
