# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-26 10:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
        ('guide', '0008_auto_20170120_2337'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProblemFlag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue', models.CharField(blank=True, choices=[('no longer exists', 'no longer exists'), ('description is inaccurate/unclear', 'description is inaccurate/unclear'), ('loose hold(s)', 'loose hold(s)'), ('other', 'other')], max_length=100)),
                ('decription', models.TextField(blank=True, help_text='a short description of the issue', null=True)),
                ('resolved', models.BooleanField(default=False)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('member', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='members.Member')),
                ('problem', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='guide.BaseProblem')),
            ],
        ),
    ]
