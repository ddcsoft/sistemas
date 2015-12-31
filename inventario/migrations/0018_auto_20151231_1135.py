# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0017_detalle_movimiento_movimiento'),
    ]

    operations = [
        migrations.AddField(
            model_name='movimiento',
            name='puesto',
            field=models.ForeignKey(default=1, to='inventario.Puesto'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movimiento',
            name='tipomvto',
            field=models.ForeignKey(default=1, to='inventario.TipoMvto'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movimiento',
            name='ubicacion',
            field=models.ForeignKey(default=1, to='inventario.Ubicacion'),
            preserve_default=False,
        ),
    ]
