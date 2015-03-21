# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import yarntail.models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('yarntail', '0014_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('test_list', yarntail.models.ListField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='pattern',
            name='design',
            field=yarntail.models.ListField(default=datetime.datetime(2015, 3, 21, 3, 25, 34, 676000, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pattern',
            name='difficulty',
            field=models.CharField(default=b'Easy', max_length=10),
            preserve_default=True,
        ),
    ]
