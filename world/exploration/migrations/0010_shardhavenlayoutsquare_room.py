# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-05 20:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0009_remove_objectdb_db_player'),
        ('exploration', '0009_auto_20181105_1906'),
    ]

    operations = [
        migrations.AddField(
            model_name='shardhavenlayoutsquare',
            name='room',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shardhaven_room', to='objects.ObjectDB'),
        ),
    ]
