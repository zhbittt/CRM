# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-07 03:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_auto_20171207_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='questionnaire',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Questionnaire', verbose_name='所属问卷'),
        ),
        migrations.AlterField(
            model_name='question',
            name='tp',
            field=models.IntegerField(choices=[(1, '打分'), (2, '单选'), (3, '评价')], default=1),
        ),
    ]
