# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0020_auto_20151231_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalle_movimiento',
            name='articulo',
            field=models.ForeignKey(to='inventario.Articulo', unique=True),
        ),
    ]
