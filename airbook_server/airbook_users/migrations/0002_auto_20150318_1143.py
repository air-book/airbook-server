# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('airbook_users', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cartitem',
            unique_together=set([('user', 'book')]),
        ),
        migrations.AlterUniqueTogether(
            name='wishitem',
            unique_together=set([('user', 'book')]),
        ),
    ]
