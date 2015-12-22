# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('principal', '0003_account_is_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='email',
        ),
        migrations.RemoveField(
            model_name='account',
            name='full_name',
        ),
        migrations.RemoveField(
            model_name='account',
            name='is_admin',
        ),
        migrations.RemoveField(
            model_name='account',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='account',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='account',
            name='password',
        ),
        migrations.RemoveField(
            model_name='account',
            name='user_name',
        ),
        migrations.AddField(
            model_name='account',
            name='is_ONG',
            field=models.BooleanField(default=False, verbose_name=b'ONG'),
        ),
        migrations.AddField(
            model_name='account',
            name='user',
            field=models.OneToOneField(default=1, verbose_name=b'Usuario', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
