# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0018_auto_20151231_1135'),
    ]

    operations = [
        migrations.AddField(
            model_name='movimiento',
            name='fecha_Retorno',
            field=models.DateField(null=True, blank=True),
        ),
    ]
