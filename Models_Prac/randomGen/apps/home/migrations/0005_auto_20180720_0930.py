# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-20 14:30
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20180720_0929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thought',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 20, 9, 30, 37, 661000)),
        ),
        migrations.AlterField(
            model_name='thought',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 20, 9, 30, 37, 661000)),
        ),
    ]