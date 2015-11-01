# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='locationmodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created At', null=True),
        ),
        migrations.AddField(
            model_name='locationmodel',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Last Updated At', null=True),
        ),
        migrations.AlterField(
            model_name='locationmodel',
            name='lat',
            field=models.FloatField(verbose_name='Latitude', blank=True),
        ),
        migrations.AlterField(
            model_name='locationmodel',
            name='lng',
            field=models.FloatField(verbose_name='Longitude', blank=True),
        ),
    ]
