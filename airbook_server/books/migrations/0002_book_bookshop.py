# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='bookshop',
            field=models.ForeignKey(default=1, to='books.BookShop'),
            preserve_default=False,
        ),
    ]
