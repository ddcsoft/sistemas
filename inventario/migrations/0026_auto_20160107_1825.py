# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-07 23:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import inventario.models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0025_auto_20160107_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='registradoPor',
            field=models.ForeignKey(default=inventario.models.iduser, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
