from django.db import models
#from django.contrib.auth.models import User


class BookShop(models.Model):
    name = models.CharField(max_length=200)


class BookAuthor(models.Model):
    author = models.CharField(max_length=200)


class BookCategory(models.Model):
    category = models.CharField(max_lenght=16, choices=BOOK_CATEGORIES)


class Book(models.Model):
    bookshop = models.ForeignKey(BookShop)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    categories = models.ManyToManyField(BookCategory)
    authors = models.ManyToManyField(BookAuthor)
    price = models.FloatField()
    publication_year = models.IntegerField(null=True, blank=True)
    editor = models.CharField(max_length=200)
    isbn_code = models.Charfield(max_length=100, null=True, blank=True)


class BookImage(models.Model):
    book = models.ForeignKey(Book)
    image = models.ImageField(upload_to="book_images", related_name="images")







