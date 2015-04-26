# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('soporte', '0003_auto_20150426_0014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acciones',
            name='fecha',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='acciones',
            name='hora',
            field=models.TimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='requerimiento',
            name='fecha_fin',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='requerimiento',
            name='fecha_inicio',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='requerimiento',
            name='hora_fin',
            field=models.TimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='requerimiento',
            name='hora_incio',
            field=models.TimeField(null=True, blank=True),
        ),
    ]
