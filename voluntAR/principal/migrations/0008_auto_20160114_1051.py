# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0007_account_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='picture',
            field=models.CharField(max_length=500, null=True, verbose_name=b'Imagen'),
        ),
    ]
