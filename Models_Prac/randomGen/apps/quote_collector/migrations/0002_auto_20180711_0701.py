# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-11 12:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quote_collector', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quote',
            name='user',
        ),
        migrations.DeleteModel(
            name='Quote',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
