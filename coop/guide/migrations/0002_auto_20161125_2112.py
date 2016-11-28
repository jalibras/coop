# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-25 21:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='exists',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='problem',
            name='comments',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='problem',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='problem',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='problem',
            name='grade',
            field=models.CharField(blank=True, choices=[('?', '?'), ('3', '3'), ('3+', '3+'), ('4', '4'), ('4+', '4+'), ('5', '5'), ('5+', '5+'), ('6A', '6A'), ('6A+', '6A+'), ('6B', '6B'), ('6B+', '6B+'), ('6C', '6C'), ('6C+', '6C+'), ('7A', '7A'), ('7A+', '7A+'), ('7B', '7B'), ('7B+', '7B+'), ('7C', '7C'), ('7C+', '7C+')], default='?', max_length=50),
        ),
    ]
