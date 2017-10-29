# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('indizio', '0006_auto_20171028_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scelta',
            name='indizio_from',
            field=models.ForeignKey(null=True, to='indizio.Indizio', related_name='fromz'),
        ),
        migrations.AlterField(
            model_name='scelta',
            name='indizio_next',
            field=models.ForeignKey(null=True, to='indizio.Indizio', related_name='toz'),
        ),
    ]
