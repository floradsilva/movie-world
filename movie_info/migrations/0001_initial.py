# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('c_type', models.CharField(max_length=20)),
                ('value', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('movie_length', models.IntegerField(default=0)),
                ('movie_release_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('r_movie', models.ForeignKey(to='movie_info.Movie')),
                ('taxonomy', models.ForeignKey(to='movie_info.Category')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='c_movie',
            field=models.ManyToManyField(to='movie_info.Movie', through='movie_info.Relationship'),
        ),
    ]
