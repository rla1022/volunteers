# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-14 01:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hours', '0012_auto_20170914_0135'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hourslocation',
            old_name='owwer',
            new_name='owner',
        ),
    ]