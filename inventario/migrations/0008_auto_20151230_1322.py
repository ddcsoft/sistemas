# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0007_auto_20151230_1011'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='marca',
            options={'ordering': ['descripcion']},
        ),
    ]
