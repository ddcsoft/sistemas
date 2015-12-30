# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0009_auto_20151230_1329'),
    ]

    operations = [
        migrations.AddField(
            model_name='puesto',
            name='area',
            field=models.ForeignKey(default=1, to='inventario.Area'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='puesto',
            name='empresa',
            field=models.ForeignKey(default=1, to='inventario.Empresa'),
            preserve_default=False,
        ),
    ]
