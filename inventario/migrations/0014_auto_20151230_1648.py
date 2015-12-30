# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0013_auto_20151230_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='medida',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
