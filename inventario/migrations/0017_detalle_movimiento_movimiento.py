# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0016_auto_20151231_0906'),
    ]

    operations = [
        migrations.AddField(
            model_name='detalle_movimiento',
            name='movimiento',
            field=models.ForeignKey(default=1, to='inventario.Movimiento'),
            preserve_default=False,
        ),
    ]
