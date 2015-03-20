# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('yarntail', '0008_auto_20150314_1005'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pattern',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=128)),
                ('description', models.CharField(max_length=3000)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(related_name=b'patterns', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
