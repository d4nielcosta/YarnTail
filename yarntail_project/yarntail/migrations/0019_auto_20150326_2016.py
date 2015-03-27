# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yarntail', '0018_auto_20150326_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pattern',
            name='difficulty',
            field=models.CharField(default=b'Easy', max_length=10, choices=[(b'Hard', b'Hard'), (b'Medium', b'Medium'), (b'Easy', b'Easy')]),
        ),
    ]
