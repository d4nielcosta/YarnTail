# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('yarntail', '0002_auto_20150312_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pattern',
            name='user',
            field=models.ForeignKey(related_name=b'patterns', to=settings.AUTH_USER_MODEL),
        ),
    ]
