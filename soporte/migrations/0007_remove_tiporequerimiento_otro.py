# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-05 04:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('soporte', '0006_tiporequerimiento_otro'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tiporequerimiento',
            name='otro',
        ),
    ]
