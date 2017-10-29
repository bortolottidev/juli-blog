# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('indizio', '0003_auto_20171025_1640'),
    ]

    operations = [
        migrations.AddField(
            model_name='indizio',
            name='id',
            field=models.AutoField(verbose_name='ID', auto_created=True, default=1, serialize=False, primary_key=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='indizio',
            name='title',
            field=models.CharField(max_length=30),
        ),
    ]
