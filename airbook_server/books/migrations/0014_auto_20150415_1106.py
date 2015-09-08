# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0013_auto_20150415_1053'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='heigth',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='book',
            name='page_number',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='book',
            name='width',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
