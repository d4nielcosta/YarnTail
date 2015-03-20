# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('yarntail', '0010_pattern_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='slug',
            field=models.SlugField(default=datetime.date(2015, 3, 14), unique=True),
            preserve_default=False,
        ),
    ]
