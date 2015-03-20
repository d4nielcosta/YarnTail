# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('yarntail', '0007_auto_20150313_1501'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='email',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(default=datetime.date(2015, 3, 14), upload_to=b'profile_images', blank=True),
            preserve_default=False,
        ),
    ]
