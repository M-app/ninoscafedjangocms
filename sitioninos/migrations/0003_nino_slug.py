# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-29 18:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitioninos', '0002_nino_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='nino',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
