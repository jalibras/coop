# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-05 11:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_member'),
        ('guide', '0003_problemvideo'),
    ]

    operations = [
        migrations.AddField(
            model_name='problemvideo',
            name='member',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='members.Member'),
        ),
        migrations.AlterField(
            model_name='problemvideo',
            name='url',
            field=models.URLField(blank=True, null=True, verbose_name='URL'),
        ),
    ]
