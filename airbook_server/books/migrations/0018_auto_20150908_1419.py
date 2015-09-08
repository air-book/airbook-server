# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0017_auto_20150415_1526'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookauthor',
            name='author',
        ),
        migrations.AddField(
            model_name='bookauthor',
            name='name',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bookauthor',
            name='nationality',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bookauthor',
            name='surname',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
