# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0012_auto_20150408_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(to='books.BookAuthor', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='editor',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.FloatField(null=True, blank=True),
        ),
    ]
