# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-25 22:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=15)),
                ('detalle_area', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Area',
                'verbose_name_plural': 'Areas',
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=11)),
                ('tipo_cliente', models.CharField(max_length=11)),
                ('informacion_adicional', models.TextField(blank=True, null=True)),
                ('datos_cliente', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.Person')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='Detalle_Venta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.CharField(max_length=15)),
                ('cantidad', models.IntegerField(default=0)),
                ('importe', models.FloatField(default=0.0)),
                ('servicio_ofrecido', models.CharField(max_length=15)),
                ('precio_unitario', models.FloatField(default=0.0)),
                ('precio_total', models.FloatField(default=0.0)),
            ],
            options={
                'verbose_name': 'DetalleVenta',
                'verbose_name_plural': 'DetalleVentas',
            },
        ),
        migrations.CreateModel(
            name='Doc_Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_documento', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name': 'Doc_Type',
                'verbose_name_plural': 'Doc_Types',
            },
        ),
        migrations.CreateModel(
            name='Forma_de_pago',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forma_pago', models.CharField(max_length=15)),
                ('tipo_moneda', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name': 'Forma_de_pago',
                'verbose_name_plural': 'Forma_de_pagos',
            },
        ),
        migrations.CreateModel(
            name='Habitacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=False)),
                ('numero', models.CharField(max_length=15)),
                ('piso', models.CharField(max_length=10)),
                ('precio_diario', models.FloatField(default=0.0)),
                ('tipo_habitacion', models.CharField(max_length=60)),
                ('foto', models.ImageField(blank=True, upload_to='')),
                ('caracteristicas', models.TextField(blank=True, null=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Habitacion',
                'verbose_name_plural': 'Habitaciones',
            },
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('costo_alojamiento', models.FloatField(default=0.0)),
                ('estado', models.BooleanField(default=False)),
                ('tipo_reserva', models.CharField(max_length=15)),
                ('fecha_ingresa', models.DateTimeField(blank=True, null=True)),
                ('fecha_reserva', models.DateTimeField(blank=True, null=True)),
                ('fecha_salida', models.DateTimeField(blank=True, null=True)),
                ('forma_de_pago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.Forma_de_pago')),
            ],
            options={
                'verbose_name': 'Reservacion',
                'verbose_name_plural': 'Reservaciones',
            },
        ),
        migrations.CreateModel(
            name='Trabajador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cargo', models.CharField(max_length=15)),
                ('estado', models.BooleanField(default=False)),
                ('fecha_inicio', models.DateTimeField(blank=True, null=True)),
                ('fecha_fin', models.DateTimeField(blank=True, null=True)),
                ('informacion_adicional', models.TextField(blank=True, null=True)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.Area')),
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.Person')),
            ],
            options={
                'verbose_name': 'Trabajador',
                'verbose_name_plural': 'Trabajadores',
            },
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(max_length=15)),
                ('numDoc', models.CharField(max_length=15)),
                ('estado', models.BooleanField(default=False)),
                ('igv', models.CharField(max_length=5)),
                ('serie', models.CharField(max_length=15)),
                ('numero_reservacion', models.IntegerField()),
                ('fecha', models.DateTimeField(auto_now_add=True, null=True)),
                ('cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hotel.Cliente')),
                ('doc_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.Doc_Type')),
                ('vendedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Venta',
                'verbose_name_plural': 'Ventas',
            },
        ),
        migrations.AddField(
            model_name='detalle_venta',
            name='venta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.Venta'),
        ),
    ]
