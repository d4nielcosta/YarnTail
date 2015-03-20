# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('yarntail', '0004_auto_20150312_1713'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=75)),
                ('date_of_birth', models.DateField()),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='comment',
            name='pattern',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='pattern',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='pattern',
            name='user',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='comment',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='favorited_pattern',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='favorited_user',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='liked_pattern',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='liked_user',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='pattern',
        ),
        migrations.DeleteModel(
            name='Pattern',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
