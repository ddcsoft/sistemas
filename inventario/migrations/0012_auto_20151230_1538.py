# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0011_auto_20151230_1537'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tipoarticulo',
            options={'ordering': ['descripcion']},
        ),
    ]
