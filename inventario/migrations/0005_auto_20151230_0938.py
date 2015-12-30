# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0004_auto_20151230_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='apellidoM',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
