# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0022_auto_20151231_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='serie',
            field=models.CharField(default=1, unique=True, max_length=100),
            preserve_default=False,
        ),
    ]
