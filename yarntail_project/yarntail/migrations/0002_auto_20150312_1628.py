# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yarntail', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.AddField(
            model_name='comment',
            name='profile',
            field=models.ForeignKey(related_name=b'comments', to='yarntail.Profile', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='pattern',
            field=models.ForeignKey(related_name=b'comments', to='yarntail.Pattern', null=True),
        ),
    ]
