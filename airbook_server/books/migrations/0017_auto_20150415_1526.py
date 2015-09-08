# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0016_auto_20150415_1457'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='publish',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='book',
            name='saleable',
            field=models.BooleanField(default=False),
        ),
    ]
