# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20150130_1651'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='authors_again',
            new_name='authors',
        ),
    ]
