# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0006_puesto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='empleado',
            name='empresa',
            field=models.ForeignKey(default=1, to='inventario.Empresa'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='empleado',
            name='area',
            field=models.ForeignKey(default=1, to='inventario.Area'),
            preserve_default=False,
        ),
    ]
