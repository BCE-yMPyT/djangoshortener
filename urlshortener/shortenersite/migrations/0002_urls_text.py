# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-28 09:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortenersite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='urls',
            name='text',
            field=models.TextField(default=''),
        ),
    ]
