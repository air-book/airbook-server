# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0015_book_conditions_detail'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookcategory',
            options={'ordering': ['order']},
        ),
        migrations.RenameField(
            model_name='book',
            old_name='categories',
            new_name='tags',
        ),
        migrations.RenameField(
            model_name='bookcategory',
            old_name='category',
            new_name='tags',
        ),
        migrations.AddField(
            model_name='bookcategory',
            name='order',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(to='books.BookAuthor'),
        ),
    ]
