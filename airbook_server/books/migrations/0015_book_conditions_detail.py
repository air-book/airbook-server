# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0014_auto_20150415_1106'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='conditions_detail',
            field=jsonfield.fields.JSONField(null=True, blank=True),
        ),
    ]
