# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-18 01:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exploration', '0037_shardhaven_weight_no_treasure_backtrack'),
    ]

    operations = [
        migrations.AddField(
            model_name='shardhaven',
            name='auto_combat',
            field=models.BooleanField(default=False, verbose_name=b'Manage Combat Automatically'),
        ),
    ]
