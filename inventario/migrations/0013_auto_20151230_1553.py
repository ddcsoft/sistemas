# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0012_auto_20151230_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='comentario',
            field=models.CharField(max_length=300, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='serie',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
