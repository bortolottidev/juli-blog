# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('indizio', '0002_auto_20171025_1627'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scelta',
            old_name='choice_text',
            new_name='text',
        ),
    ]
