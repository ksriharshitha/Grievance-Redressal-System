# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-10 05:51
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaint', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academics',
            name='fidate',
            field=models.DateField(default=datetime.datetime(2018, 12, 10, 0, 0)),
        ),
        migrations.AlterField(
            model_name='events',
            name='fidate',
            field=models.DateField(default=datetime.datetime(2018, 12, 10, 0, 0)),
        ),
        migrations.AlterField(
            model_name='hostel',
            name='fidate',
            field=models.DateField(default=datetime.datetime(2018, 12, 10, 0, 0)),
        ),
        migrations.AlterField(
            model_name='others',
            name='fidate',
            field=models.DateField(default=datetime.datetime(2018, 12, 10, 0, 0)),
        ),
        migrations.AlterField(
            model_name='sports',
            name='fidate',
            field=models.DateField(default=datetime.datetime(2018, 12, 10, 0, 0)),
        ),
    ]