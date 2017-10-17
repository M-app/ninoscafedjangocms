# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('sitioninos', '0009_auto_20171017_1553'),
    ]

    operations = [
        migrations.CreateModel(
            name='NinoPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, related_name='ninos_integration_ninopluginmodel', parent_link=True, to='cms.CMSPlugin')),
                ('nino', models.ForeignKey(to='sitioninos.Nino')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
