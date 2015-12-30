# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0010_auto_20151230_1334'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articulo',
            options={'ordering': ['descripcion']},
        ),
        migrations.AlterModelOptions(
            name='clasificacion',
            options={'ordering': ['descripcion']},
        ),
        migrations.AlterModelOptions(
            name='estadoarticulo',
            options={'ordering': ['descripcion']},
        ),
        migrations.AlterModelOptions(
            name='puesto',
            options={'ordering': ['descripcion']},
        ),
        migrations.AlterModelOptions(
            name='tipomvto',
            options={'ordering': ['descripcion']},
        ),
        migrations.AlterModelOptions(
            name='ubicacion',
            options={'ordering': ['descripcion']},
        ),
    ]
