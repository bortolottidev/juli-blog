# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('indizio', '0004_auto_20171028_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indizio',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='scelta',
            name='indizio_from',
            field=models.ForeignKey(related_name='from+', null=True, to='indizio.Indizio'),
        ),
        migrations.AlterField(
            model_name='scelta',
            name='indizio_next',
            field=models.ForeignKey(related_name='goto+', null=True, to='indizio.Indizio'),
        ),
    ]
