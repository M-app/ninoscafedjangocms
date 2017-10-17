# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('ninos_integration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hola',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, related_name='ninos_integration_hola', parent_link=True, to='cms.CMSPlugin')),
                ('nombre_invitado', models.CharField(max_length=50, default='Invitado')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
