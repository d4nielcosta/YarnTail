# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yarntail', '0016_pattern_design'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pattern',
            name='design',
            field=models.CharField(default=b'empty pattern', max_length=100000),
        ),
    ]
