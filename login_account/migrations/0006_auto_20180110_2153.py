# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-10 21:53
from __future__ import unicode_literals

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_account', '0005_auto_20180110_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(default=django.contrib.auth.models.User, max_length=200, verbose_name='auth.User'),
        ),
    ]
