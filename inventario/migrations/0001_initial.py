# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=150)),
                ('modelo', models.CharField(max_length=150)),
                ('serie', models.CharField(max_length=100)),
                ('comentario', models.CharField(max_length=300)),
                ('medida', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Clasificacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Detalle_Movimiento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='EstadoArticulo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Movimiento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_registro', models.DateField()),
                ('fecha_Mvto', models.DateField()),
                ('Comentario', models.CharField(max_length=200)),
                ('registradoPor', models.ForeignKey(related_name='Reg_Mvto', to=settings.AUTH_USER_MODEL)),
                ('responsable', models.ForeignKey(related_name='Res_Mvto', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TipoArticulo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='TipoMvto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Ubicacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Ubicacion_Articulo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('articulo', models.ForeignKey(to='inventario.Articulo')),
                ('movimiento', models.ForeignKey(to='inventario.Movimiento')),
                ('ubicacion', models.ForeignKey(to='inventario.Ubicacion')),
            ],
        ),
        migrations.AddField(
            model_name='articulo',
            name='clasificacion',
            field=models.ForeignKey(to='inventario.Clasificacion'),
        ),
        migrations.AddField(
            model_name='articulo',
            name='empresa',
            field=models.ForeignKey(to='inventario.Empresa'),
        ),
        migrations.AddField(
            model_name='articulo',
            name='estado',
            field=models.ForeignKey(to='inventario.EstadoArticulo'),
        ),
        migrations.AddField(
            model_name='articulo',
            name='marca',
            field=models.ForeignKey(to='inventario.Marca'),
        ),
        migrations.AddField(
            model_name='articulo',
            name='registradoPor',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='articulo',
            name='tipo',
            field=models.ForeignKey(to='inventario.TipoArticulo'),
        ),
    ]
