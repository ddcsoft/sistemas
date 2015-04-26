# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('soporte', '0002_auto_20150425_2331'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='acciones',
            options={'verbose_name_plural': 'Acciones'},
        ),
        migrations.AlterField(
            model_name='acciones',
            name='fecha',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='acciones',
            name='hora',
            field=models.TimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='requerimiento',
            name='fecha_fin',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='requerimiento',
            name='fecha_inicio',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='requerimiento',
            name='hora_fin',
            field=models.TimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='requerimiento',
            name='hora_incio',
            field=models.TimeField(blank=True),
        ),
    ]
