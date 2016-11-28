# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-28 13:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=300, null=True)),
                ('grade', models.CharField(blank=True, choices=[('?', '?'), ('3', '3'), ('3+', '3+'), ('4', '4'), ('4+', '4+'), ('5', '5'), ('5+', '5+'), ('6A', '6A'), ('6A+', '6A+'), ('6B', '6B'), ('6B+', '6B+'), ('6C', '6C'), ('6C+', '6C+'), ('7A', '7A'), ('7A+', '7A+'), ('7B', '7B'), ('7B+', '7B+'), ('7C', '7C'), ('7C+', '7C+')], default='?', max_length=50)),
                ('steepness', models.CharField(blank=True, choices=[('slab', 'slab'), ('vert', 'vertical'), ('slov', 'slight overhang'), ('over', 'overhang'), ('exov', 'extreme overhang'), ('na', 'not applicable')], max_length=50, null=True)),
                ('hold_colour', models.CharField(blank=True, max_length=300, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('picture_1', models.FileField(blank=True, null=True, upload_to='uploads')),
                ('picture_2', models.FileField(blank=True, null=True, upload_to='uploads')),
                ('picture_3', models.FileField(blank=True, null=True, upload_to='uploads')),
                ('videos', models.CharField(blank=True, default='', max_length=1000, null=True)),
                ('comments', models.TextField(blank=True, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('setter', models.CharField(blank=True, max_length=300, null=True)),
                ('exists', models.BooleanField(default=True)),
            ],
        ),
    ]
