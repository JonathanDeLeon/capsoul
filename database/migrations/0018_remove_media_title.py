# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-27 19:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0017_auto_20171127_1923'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='media',
            name='title',
        ),
    ]
