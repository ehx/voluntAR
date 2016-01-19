# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0013_auto_20160119_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventback',
            name='event',
            field=models.OneToOneField(verbose_name=b'Evento', to='principal.Event'),
        ),
    ]
