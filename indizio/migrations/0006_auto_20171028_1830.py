# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('indizio', '0005_auto_20171028_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scelta',
            name='indizio_from',
            field=models.ForeignKey(null=True, related_name='fdsfsd', to='indizio.Indizio'),
        ),
        migrations.AlterField(
            model_name='scelta',
            name='indizio_next',
            field=models.ForeignKey(null=True, related_name='goto', to='indizio.Indizio'),
        ),
    ]
