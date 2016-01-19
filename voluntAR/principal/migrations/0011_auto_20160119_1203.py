# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0010_auto_20160119_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventback',
            name='event',
            field=models.ForeignKey(verbose_name=b'Evento', to='principal.Event'),
        ),
    ]
