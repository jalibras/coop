# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-30 09:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0012_merge_20170126_1203'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='posted_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]