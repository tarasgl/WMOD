# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-16 13:02
from __future__ import unicode_literals

from django.db import migrations, models
import location_field.models.plain


class Migration(migrations.Migration):

    dependencies = [
        ('mapapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='marker',
            name='city',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='marker',
            name='location',
            field=location_field.models.plain.PlainLocationField(default=1.0, max_length=63),
            preserve_default=False,
        ),
    ]