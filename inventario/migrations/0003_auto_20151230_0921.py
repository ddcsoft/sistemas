# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0002_articulo_codigo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('apellidoP', models.CharField(max_length=50)),
                ('apellidoM', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='movimiento',
            name='responsable',
            field=models.ForeignKey(to='inventario.Empleado'),
        ),
    ]
