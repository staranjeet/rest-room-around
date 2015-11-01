# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LocationModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.CharField(max_length=255, null=True, verbose_name=b'Location of the rest room', blank=True)),
                ('lat', models.FloatField(blank=True)),
                ('lng', models.FloatField(blank=True)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326, geography=True, null=True, verbose_name=b'Longitude/Latitude', blank=True)),
            ],
            options={
                'db_table': 'restroom',
                'verbose_name_plural': 'Rest Rooms Location',
            },
        ),
    ]
