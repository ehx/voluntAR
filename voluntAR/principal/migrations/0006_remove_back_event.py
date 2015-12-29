# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0005_auto_20151229_1109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='back',
            name='event',
        ),
    ]
