# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-27 06:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feb15_schools_comezo', '0007_auto_20170227_1203'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher_info',
            name='password',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
