# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-16 01:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TBLSessions', '0003_auto_20180102_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tblsession',
            name='title',
            field=models.CharField(help_text='Session title.', max_length=200, verbose_name='Title'),
        ),
    ]