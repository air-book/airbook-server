# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0019_auto_20150908_1516'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.CharField(blank=True, max_length=30, null=True, choices=[(b'COPERTINA MORBIDA', b'Copertina Morbida'), (b'COPERTINA RIGIDA', b'Copertina Rigida')]),
        ),
        migrations.AddField(
            model_name='book',
            name='weigth',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='bookcategorytype',
            name='type',
            field=models.CharField(blank=True, max_length=30, null=True, choices=[(b'PRIMA EDIZIONE', b'Prima Edizione'), (b'BROSSURA', b'Brossura'), (b'EDIZIONE ECONOMICA', b'Edizione Economica'), (b'LIBRO ANTICO', b'Libro Antico'), (b'LIBRO AUTOGRAFATO', b'Libro Autografato'), (b'LIBRO D ARTISTA', b'Libro d Artista')]),
        ),
    ]
