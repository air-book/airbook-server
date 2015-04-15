# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0011_auto_20150326_0759'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookimage',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='bookimage',
            name='order',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(to='books.BookAuthor'),
        ),
        migrations.AlterField(
            model_name='book',
            name='categories',
            field=models.ManyToManyField(to='books.BookTags'),
        ),
    ]
