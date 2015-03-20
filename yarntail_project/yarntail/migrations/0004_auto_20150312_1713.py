# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('yarntail', '0003_auto_20150312_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='favorited_pattern',
            field=models.ForeignKey(related_name=b'users_that_favorite_this', to='yarntail.Pattern', null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='favorited_user',
            field=models.ForeignKey(related_name=b'users_that_favorite_this', to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='liked_pattern',
            field=models.ForeignKey(related_name=b'users_that_like_this', to='yarntail.Pattern', null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='liked_user',
            field=models.ForeignKey(related_name=b'users_that_like_this', to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
