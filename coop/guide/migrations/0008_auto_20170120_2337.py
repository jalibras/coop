# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-20 23:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0007_areaimage_imagemapcode'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sector',
            options={'ordering': ('name',)},
        ),
        migrations.AlterField(
            model_name='artificialproblem',
            name='holds',
            field=models.CharField(blank=True, choices=[('Black', 'Black'), ('Blue', 'Blue'), ('Blue (Dark)', 'Blue (Dark)'), ('Brown', 'Brown'), ('Cappucino', 'Cappucino'), ('Green', 'Green'), ('Green (Dark)', 'Green (Dark)'), ('Green (Flouro)', 'Green (Flouro)'), ('Grey', 'Grey'), ('Mint', 'Mint'), ('Orange', 'Orange'), ('Pink', 'Pink'), ('Purple', 'Purple'), ('Red', 'Red'), ('Red (Dark)', 'Red (Dark)'), ('Red (Rust)', 'Red (Rust)'), ('White', 'White'), ('Wooden', 'Wooden'), ('Yellow', 'Yellow'), ('Yellow (Flouro)', 'Yellow (Flouro)'), ('N/A (see description)', 'N/A (see description)')], max_length=300, null=True, verbose_name='hold colour'),
        ),
        migrations.AlterField(
            model_name='baseproblem',
            name='grade',
            field=models.CharField(blank=True, choices=[('?', '?'), ('3', '3'), ('3+', '3+'), ('4', '4'), ('4+', '4+'), ('5', '5'), ('5+', '5+'), ('6A', '6A'), ('6A+', '6A+'), ('6B', '6B'), ('6B+', '6B+'), ('6C', '6C'), ('6C+', '6C+'), ('7A', '7A'), ('7A+', '7A+'), ('7B', '7B'), ('7B+', '7B+'), ('7C', '7C'), ('7C+', '7C+')], default='?', help_text='We use the <a href="https://en.wikipedia.org/wiki/Grade_(bouldering)#Fontainebleau_grades" target="_blank">Font grading system</a> for bouldering problems', max_length=50),
        ),
    ]
