# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('soporte', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tiporequerimiento',
            old_name='nombre',
            new_name='descripcion',
        ),
        migrations.AddField(
            model_name='acciones',
            name='descripcion',
            field=models.CharField(default='req 1', max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='requerimiento',
            name='descripcion',
            field=models.CharField(default='req 3', max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='requerimiento',
            name='status',
            field=models.BooleanField(default='tttt'),
            preserve_default=False,
        ),
    ]
