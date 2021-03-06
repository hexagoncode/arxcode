# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-01-22 00:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('character', '0004_auto_20161217_0654'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cluediscovery',
            options={'verbose_name_plural': 'Clue Discoveries'},
        ),
        migrations.AlterModelOptions(
            name='mysterydiscovery',
            options={'verbose_name_plural': 'Mystery Discoveries'},
        ),
        migrations.AlterModelOptions(
            name='revelationdiscovery',
            options={'verbose_name_plural': 'Revelation Discoveries'},
        ),
        migrations.AlterUniqueTogether(
            name='mysterydiscovery',
            unique_together=set([('character', 'mystery')]),
        ),
        migrations.AlterUniqueTogether(
            name='revelationdiscovery',
            unique_together=set([('character', 'revelation')]),
        ),
        migrations.AlterUniqueTogether(
            name='rosterentry',
            unique_together=set([('player', 'character')]),
        ),
    ]
