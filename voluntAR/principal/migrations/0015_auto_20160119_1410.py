# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0014_auto_20160119_1219'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='logo',
            new_name='avatar',
        ),
    ]
