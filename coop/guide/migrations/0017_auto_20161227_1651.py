# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-27 16:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0016_auto_20161227_1648'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MemberByProblem',
            new_name='ProblemByMember',
        ),
    ]
