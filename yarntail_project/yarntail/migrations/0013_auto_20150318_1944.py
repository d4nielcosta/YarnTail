# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yarntail', '0012_auto_20150314_1754'),
    ]

    operations = [
        migrations.AddField(
            model_name='pattern',
            name='likes',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pattern',
            name='views',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
    ]
