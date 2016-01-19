# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0012_auto_20160119_1204'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='eventvoluntary',
            unique_together=set([('event', 'voluntary')]),
        ),
    ]
