# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yarntail', '0014_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='pattern',
            name='difficulty',
            field=models.CharField(default=b'Easy', max_length=10),
            preserve_default=True,
        ),
    ]
