# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-05 12:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0006_auto_20161205_1215'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='problemvideo',
            name='url',
        ),
    ]