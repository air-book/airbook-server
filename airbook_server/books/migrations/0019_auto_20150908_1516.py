# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0018_auto_20150908_1419'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookCategoryType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(blank=True, max_length=30, null=True, choices=[(b'PRIMA EDIZIONE', b'Prima Edizione'), (b'BROSSURA', b'Brossura'), (b'COPERTINA MORBIDA', b'Copertina Morbida'), (b'LIBRO ANTICO', b'Libro Antico'), (b'LIBRO AUTOGRAFATO', b'Libro Autografato'), (b'LIBRO D ARTISTA', b'Libro d Artista')])),
                ('icon', models.ImageField(upload_to=b'category_type_image')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='category_type',
            field=models.ManyToManyField(to='books.BookCategoryType'),
        ),
    ]
