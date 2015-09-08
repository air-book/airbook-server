# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0025_auto_20150908_2148'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookauthor',
            name='surname',
        ),
    ]
