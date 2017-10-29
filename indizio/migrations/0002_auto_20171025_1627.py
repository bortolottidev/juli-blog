# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('indizio', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scelta',
            name='indizio',
        ),
        migrations.AddField(
            model_name='scelta',
            name='indizio_from',
            field=models.ForeignKey(to='indizio.Indizio', null=True, related_name='From'),
        ),
        migrations.AddField(
            model_name='scelta',
            name='indizio_next',
            field=models.ForeignKey(to='indizio.Indizio', null=True, related_name='GoTo'),
        ),
    ]
