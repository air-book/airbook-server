# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0021_auto_20150908_1558'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookshop',
            name='tags',
            field=models.ManyToManyField(to='books.BookCategory', null=True, blank=True),
        ),
    ]
