# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0006_remove_back_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='logo',
            field=models.CharField(default='aaaa', max_length=500, verbose_name=b'logo'),
            preserve_default=False,
        ),
    ]
