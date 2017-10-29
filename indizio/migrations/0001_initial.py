# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Indizio',
            fields=[
                ('title', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Scelta',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('choice_text', models.CharField(max_length=200)),
                ('indizio', models.ForeignKey(to='indizio.Indizio')),
            ],
        ),
    ]
