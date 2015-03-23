# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yarntail', '0015_pattern_difficulty'),
    ]

    operations = [
        migrations.AddField(
            model_name='pattern',
            name='design',
            field=models.CharField(default=b'empty pattern', max_length=10000),
            preserve_default=True,
        ),
    ]
