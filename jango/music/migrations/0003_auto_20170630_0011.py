# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-30 07:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_song_favorite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='logo',
            field=models.FileField(upload_to=''),
        ),
    ]
