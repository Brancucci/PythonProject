# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-04-13 17:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mathisfun', '0002_remove_results_password'),
    ]

    operations = [
        migrations.RenameField(
            model_name='results',
            old_name='addition',
            new_name='average',
        ),
        migrations.RenameField(
            model_name='results',
            old_name='userid',
            new_name='userName',
        ),
        migrations.RemoveField(
            model_name='results',
            name='division',
        ),
        migrations.RemoveField(
            model_name='results',
            name='multiplication',
        ),
        migrations.RemoveField(
            model_name='results',
            name='subtraction',
        ),
        migrations.RemoveField(
            model_name='results',
            name='total',
        ),
        migrations.AddField(
            model_name='results',
            name='operator',
            field=models.IntegerField(default=0),
        ),
    ]
