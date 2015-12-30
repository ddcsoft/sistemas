# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0014_auto_20151230_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='codigo',
            field=models.CharField(unique=True, max_length=10),
        ),
    ]
