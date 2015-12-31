# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0015_auto_20151230_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='detalle_movimiento',
            name='articulo',
            field=models.ForeignKey(default=1, to='inventario.Articulo'),
            preserve_default=False,
        ),
    ]
