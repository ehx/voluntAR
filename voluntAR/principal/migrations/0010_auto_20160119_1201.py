# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0009_auto_20160114_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventback',
            name='event',
            field=models.ForeignKey(verbose_name=b'Evento', to='principal.Event', unique=True),
        ),
    ]
