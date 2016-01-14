# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0008_auto_20160114_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.CharField(max_length=500, verbose_name=b'Descripcion'),
        ),
        migrations.AlterField(
            model_name='event',
            name='finish_date',
            field=models.DateField(verbose_name=b'Fecha de Fin'),
        ),
        migrations.AlterField(
            model_name='event',
            name='owner',
            field=models.ForeignKey(related_name='accountEvent', verbose_name=b'Propietario', to='principal.Account'),
        ),
        migrations.AlterField(
            model_name='event',
            name='short_description',
            field=models.CharField(max_length=150, verbose_name=b'Descripcion Corta'),
        ),
    ]
