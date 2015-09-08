# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0023_auto_20150908_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='category_type',
            field=models.ManyToManyField(to='books.BookCategoryType', blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='tags',
            field=models.ManyToManyField(to='books.BookCategory', blank=True),
        ),
    ]
