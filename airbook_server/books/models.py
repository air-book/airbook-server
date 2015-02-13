import os
from django.db import models
#from django.contrib.auth.models import User
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill




class BookShop(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return u'%s' % self.name


class BookAuthor(models.Model):
    author = models.CharField(max_length=200)

    def __unicode__(self):
        return u'%s' % self.author


class BookCategory(models.Model):
    category = models.CharField(max_length=16)

    def __unicode__(self):
        return u'%s' % self.category


BOOK_CONDITIONS = (
    (0, 'Pessimo'),
    (1, 'Medio'),
    (2, 'Buono'),
    (3, 'Nuovo'),
)

class Book(models.Model):
    bookshop = models.ForeignKey(BookShop)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    categories = models.ManyToManyField(BookCategory)
    authors = models.ManyToManyField(BookAuthor)
    price = models.FloatField()
    publication_year = models.IntegerField(null=True, blank=True)
    editor = models.CharField(max_length=200)
    isbn_code = models.CharField(max_length=100, null=True, blank=True)
    archive_code = models.CharField(max_length=10, null=True, blank=True)
    conditions = models.IntegerField(choices=BOOK_CONDITIONS, null=True, blank=True)

    def __unicode__(self):
        return u'%s' % self.title


class BookImage(models.Model):
    book = models.ForeignKey(Book, related_name="images")
    image = models.ImageField(upload_to="book_images")
    image_thumb = ImageSpecField(source='image',
                                      processors=[ResizeToFill(400, 250)],
                                      format='JPEG',
                                      options={'quality': 90})

    def __unicode__(self):
        return u'%s' % os.path.basename(self.image.path)
