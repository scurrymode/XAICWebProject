# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-11 04:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='testImage',
            field=models.ImageField(default='noImage', upload_to='static/img/upload'),
        ),
    ]
