# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GrandSlam',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('grandslam', models.CharField(default=b'Australian Open', max_length=50, choices=[(b'Australian Open', b'Australian Open'), (b'French Open', b'French Open'), (b'Wimbledon', b'Wimbledon'), (b'US Open', b'US Open')])),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='grandslams',
            name='player',
        ),
        migrations.AddField(
            model_name='player',
            name='grandslams_won',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='player',
            name='age',
            field=models.IntegerField(),
        ),
        migrations.DeleteModel(
            name='GrandSlams',
        ),
        migrations.AddField(
            model_name='grandslam',
            name='player',
            field=models.ForeignKey(to='players.Player'),
        ),
    ]
