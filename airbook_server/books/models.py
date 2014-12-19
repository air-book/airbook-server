from django.db import models


class BookShop(models.Model):
    name = models.CharField(max_length=200)


class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    







