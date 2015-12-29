# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0004_auto_20151222_1324'),
    ]

    operations = [
        migrations.CreateModel(
            name='Back',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'Nombre')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('finish_date', models.DateField(null=True, verbose_name=b'Fecha de Fin')),
                ('picture', models.CharField(max_length=500, verbose_name=b'Imagen')),
                ('title', models.CharField(max_length=50, verbose_name=b'Titulo')),
                ('short_description', models.CharField(max_length=150, verbose_name=b'Descripcion Corta', blank=True)),
                ('description', models.CharField(max_length=500, verbose_name=b'Descripcion', blank=True)),
                ('owner', models.ForeignKey(related_name='accountEvent', verbose_name=b'Propietario', to='principal.Account', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EventBack',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='EventVoluntary',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.CharField(max_length=5000, verbose_name=b'Comentario')),
                ('done', models.BooleanField(default=0, verbose_name=b'Realizado')),
            ],
        ),
        migrations.CreateModel(
            name='BackElement',
            fields=[
                ('back_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='principal.Back')),
                ('quantity', models.IntegerField(verbose_name=b'Cantidad')),
            ],
            bases=('principal.back',),
        ),
        migrations.AddField(
            model_name='eventvoluntary',
            name='back_action',
            field=models.ManyToManyField(related_name='Acciones_Voluntario', to='principal.Back'),
        ),
        migrations.AddField(
            model_name='eventvoluntary',
            name='event',
            field=models.ForeignKey(verbose_name=b'Evento', to='principal.Event'),
        ),
        migrations.AddField(
            model_name='eventvoluntary',
            name='voluntary',
            field=models.ForeignKey(verbose_name=b'Voluntario', to='principal.Account'),
        ),
        migrations.AddField(
            model_name='eventback',
            name='back_action',
            field=models.ManyToManyField(related_name='Acciones_Evento', to='principal.Back'),
        ),
        migrations.AddField(
            model_name='eventback',
            name='event',
            field=models.ForeignKey(verbose_name=b'Evento', to='principal.Event'),
        ),
        migrations.AddField(
            model_name='back',
            name='event',
            field=models.ForeignKey(verbose_name=b'Evento', to='principal.Event'),
        ),
        migrations.AddField(
            model_name='eventvoluntary',
            name='back_element',
            field=models.ManyToManyField(related_name='Elementos_Voluntario', to='principal.BackElement'),
        ),
        migrations.AddField(
            model_name='eventback',
            name='back_element',
            field=models.ManyToManyField(related_name='Elementos_Evento', to='principal.BackElement'),
        ),
    ]
