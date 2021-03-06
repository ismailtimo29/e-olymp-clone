# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-07 14:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0002_auto_20170803_1146'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='problemtest',
            options={'verbose_name': 'ProblemTest', 'verbose_name_plural': 'ProblemTests'},
        ),
        migrations.RenameField(
            model_name='problem',
            old_name='bookmarks',
            new_name='bookmark',
        ),
        migrations.RenameField(
            model_name='problemtest',
            old_name='try_id',
            new_name='attempt',
        ),
        migrations.RemoveField(
            model_name='try',
            name='user_id',
        ),
    ]
