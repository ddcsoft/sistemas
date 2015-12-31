# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0019_movimiento_fecha_retorno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movimiento',
            name='puesto',
            field=models.ForeignKey(blank=True, to='inventario.Puesto', null=True),
        ),
    ]
