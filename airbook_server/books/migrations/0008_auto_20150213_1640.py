# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_book_conditions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(to='books.BookAuthor', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='book',
            name='categories',
            field=models.ManyToManyField(to='books.BookTags', null=True, blank=True),
            preserve_default=True,
        ),
    ]
