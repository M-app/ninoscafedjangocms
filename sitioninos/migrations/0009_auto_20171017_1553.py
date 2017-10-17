# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitioninos', '0008_auto_20171005_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nino',
            name='etapa',
            field=models.CharField(max_length=15, default='Primaria', choices=[('Primaria', 'Primaria'), ('Básico', 'Básico'), ('Diversificado', 'Diversificado')]),
        ),
    ]
