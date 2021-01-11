# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-05-28 10:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('all_models', '0003_auto_20190528_1005'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbhttpinterface',
            name='uslRedirect',
        ),
        migrations.AddField(
            model_name='tbhttpinterface',
            name='urlRedirect',
            field=models.IntegerField(db_column='urlRedirect', default=1, verbose_name='是否自动重定向'),
        ),
    ]
