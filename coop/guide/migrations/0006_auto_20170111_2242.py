# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-11 22:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0005_auto_20170110_1102'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='area',
            name='area_map_imagemap_snippet',
        ),
        migrations.AlterField(
            model_name='artificialproblem',
            name='holds',
            field=models.CharField(blank=True, choices=[('Red', 'Red'), ('Green', 'Green'), ('Blue', 'Blue'), ('Black', 'Black'), ('White', 'White'), ('Pink', 'Pink'), ('Purple', 'Purple'), ('Mint', 'Mint'), ('Grey', 'Grey'), ('Orange', 'Orange'), ('Yellow', 'Yellow'), ('Brown', 'Brown'), ('Other', 'Other')], max_length=300, null=True, verbose_name='hold colour'),
        ),
    ]