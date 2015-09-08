# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0020_auto_20150908_1550'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookShopUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='bookshop',
            name='user',
        ),
        migrations.AddField(
            model_name='bookshopuser',
            name='bookshop',
            field=models.ForeignKey(to='books.BookShop'),
        ),
        migrations.AddField(
            model_name='bookshopuser',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
