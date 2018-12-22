# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-15 20:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exploration', '0024_auto_20181115_0159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shardhavenlayout',
            name='haven',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='layouts', to='exploration.Shardhaven', unique=True),
        ),
    ]
