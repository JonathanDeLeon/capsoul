# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-27 19:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0016_auto_20171127_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='title',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]