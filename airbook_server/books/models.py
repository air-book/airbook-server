import os
from django.db import models
#from django.contrib.auth.models import User
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.contrib.auth.models import User
from jsonfield import JSONField


class BookShop(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return u'%s' % self.name


class BookAuthor(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    surname = models.CharField(max_length=200, null=True, blank=True)
    nationality = models.CharField(max_length=100, null=True, blank=True)

    def __unicode__(self):
        return u'%s %s' %(self.name, self.surname)


class BookCategory(models.Model):
    tags = models.CharField(max_length=16)
    order = models.IntegerField(null=True, blank=True, default=0)

    class Meta:
        ordering = ['order']


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
    authors = models.ManyToManyField(BookAuthor)
    price = models.FloatField(null=True, blank=True)
    publication_year = models.IntegerField(null=True, blank=True)
    editor = models.CharField(max_length=200, null=True, blank=True)
    isbn_code = models.CharField(max_length=100, null=True, blank=True)
    archive_code = models.CharField(max_length=10, null=True, blank=True)
    page_number = models.IntegerField(null=True, blank=True)
    language = models.CharField(max_length=20, null=True, blank=True)
    width = models.IntegerField(null=True, blank=True)
    heigth = models.IntegerField(null=True, blank=True)
    conditions = models.IntegerField(choices=BOOK_CONDITIONS, null=True, blank=True)
    conditions_detail = JSONField(null=True, blank=True)
    description = models.CharField(max_length=2000)
    tags = models.ManyToManyField(BookCategory)
    saleable = models.BooleanField(default=False)
    publish = models.BooleanField(default=True)


    def __unicode__(self):
        return u'%s' % self.title


    def save(self, *args, **kwargs):
        if self.price and self.editor:
            self.saleable = True
        else:
            self.saleable = False


        return super(Book, self).save(*args, **kwargs)


class BookImage(models.Model):
    book = models.ForeignKey(Book, related_name="images")
    image = models.ImageField(upload_to="book_images")
    order = models.IntegerField(null=True, blank=True, default=0)
    image_thumb = ImageSpecField(source='image',
                                      processors=[ResizeToFill(400, 250)],
                                      format='JPEG',
                                      options={'quality': 90})

    class Meta:
        ordering = ['order']

    def __unicode__(self):
        return u'%s' % os.path.basename(self.image.path)
