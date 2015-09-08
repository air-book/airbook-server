# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0022_bookshop_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='category_type',
            field=models.ManyToManyField(to='books.BookCategoryType', null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='tags',
            field=models.ManyToManyField(to='books.BookCategory', null=True),
        ),
        migrations.AlterField(
            model_name='bookshop',
            name='tags',
            field=models.ManyToManyField(to='books.BookCategory'),
        ),
    ]
