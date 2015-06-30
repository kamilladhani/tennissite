# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GrandSlams',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('won', models.CharField(max_length=200)),
                ('australian', models.CharField(max_length=200)),
                ('french', models.CharField(max_length=200)),
                ('wimbledon', models.CharField(max_length=200)),
                ('us', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('dob', models.CharField(max_length=200)),
                ('age', models.CharField(max_length=200)),
                ('desc', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='grandslams',
            name='player',
            field=models.ForeignKey(to='players.Player'),
        ),
    ]
