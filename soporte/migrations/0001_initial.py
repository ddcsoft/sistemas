# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Acciones',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Requerimiento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_inicio', models.DateField()),
                ('hora_incio', models.TimeField()),
                ('fecha_fin', models.DateField()),
                ('hora_fin', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='TipoRequerimiento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='requerimiento',
            name='tipo_requerimiento',
            field=models.ForeignKey(to='soporte.TipoRequerimiento'),
        ),
        migrations.AddField(
            model_name='acciones',
            name='requerimiento',
            field=models.ForeignKey(to='soporte.Requerimiento'),
        ),
    ]
