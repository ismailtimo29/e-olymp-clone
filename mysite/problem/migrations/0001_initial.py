# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-31 09:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmarks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Classification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Competitions',
                'verbose_name': 'Competiton',
            },
        ),
        migrations.CreateModel(
            name='Compiler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Complexity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('point', models.IntegerField()),
                ('bookmarks', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='problem.Bookmarks')),
                ('classification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='problem.Classification')),
                ('competition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='problems', to='problem.Competition')),
                ('complexity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='problem.Complexity')),
            ],
            options={
                'verbose_name_plural': 'Problems',
                'verbose_name': 'Problem',
            },
        ),
        migrations.CreateModel(
            name='Rules',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Statuses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('compiler', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='problem.Compiler')),
            ],
            options={
                'verbose_name_plural': 'Tets',
                'verbose_name': 'Test',
            },
        ),
        migrations.CreateModel(
            name='Try',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(max_length=255, unique=True)),
                ('source', models.CharField(max_length=255)),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='problem.Problem')),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='test',
            name='try_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='problem.Try'),
        ),
        migrations.AddField(
            model_name='problem',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='problem.Status'),
        ),
        migrations.AddField(
            model_name='competition',
            name='rule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='problem.Rules'),
        ),
        migrations.AddField(
            model_name='competition',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='problem.Statuses'),
        ),
        migrations.AddField(
            model_name='competition',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='problem.Type'),
        ),
    ]
