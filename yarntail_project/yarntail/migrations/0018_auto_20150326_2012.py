# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yarntail', '0017_auto_20150324_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pattern',
            name='difficulty',
            field=models.CharField(default=b'Easy', max_length=10, choices=[(b'H', b'Hard'), (b'M', b'Medium'), (b'E', b'Easy')]),
        ),
    ]
