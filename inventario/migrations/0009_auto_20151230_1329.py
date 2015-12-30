# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0008_auto_20151230_1322'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='area',
            options={'ordering': ['descripcion']},
        ),
        migrations.AlterModelOptions(
            name='empleado',
            options={'ordering': ['nombre']},
        ),
        migrations.AlterModelOptions(
            name='empresa',
            options={'ordering': ['descripcion']},
        ),
    ]
