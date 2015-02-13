# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_book_archive_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='conditions',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'Pessimo'), (1, b'Medio'), (2, b'Buono'), (3, b'Nuovo')]),
            preserve_default=True,
        ),
    ]
