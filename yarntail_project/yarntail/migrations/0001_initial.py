# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('creation_date', models.DateTimeField()),
                ('comment_string', models.CharField(max_length=2100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pattern',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=128)),
                ('pattern_string', models.CharField(max_length=20000)),
                ('description', models.CharField(max_length=3000)),
                ('creation_date', models.DateTimeField()),
                ('likes', models.IntegerField()),
                ('views', models.IntegerField()),
                ('favorites', models.IntegerField()),
                ('difficulty', models.CharField(default=b'E', max_length=1, choices=[(b'H', b'Hard'), (b'M', b'Medium'), (b'E', b'Easy')])),
                ('comment', models.ForeignKey(related_name=b'commented_pattern', to='yarntail.Comment')),
                ('user', models.OneToOneField(related_name=b'patterns', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=3000)),
                ('likes', models.IntegerField()),
                ('favorites', models.IntegerField()),
                ('views', models.IntegerField()),
                ('registration_date', models.DateTimeField()),
                ('number_of_patterns', models.IntegerField()),
                ('date_of_birth', models.DateField()),
                ('comment', models.ForeignKey(related_name=b'commented_profile', to='yarntail.Comment')),
                ('favorited_pattern', models.ForeignKey(related_name=b'users_that_favorite_this', to='yarntail.Pattern')),
                ('favorited_user', models.ForeignKey(related_name=b'users_that_favorite_this', to=settings.AUTH_USER_MODEL)),
                ('liked_pattern', models.ForeignKey(related_name=b'users_that_like_this', to='yarntail.Pattern')),
                ('liked_user', models.ForeignKey(related_name=b'users_that_like_this', to=settings.AUTH_USER_MODEL)),
                ('pattern', models.ForeignKey(to='yarntail.Pattern')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='comment',
            name='pattern',
            field=models.ForeignKey(related_name=b'comments', to='yarntail.Pattern'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(related_name=b'comments', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
