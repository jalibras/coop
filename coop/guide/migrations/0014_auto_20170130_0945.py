# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-30 09:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0013_comment_posted_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='posted_at',
            new_name='created',
        ),
    ]
