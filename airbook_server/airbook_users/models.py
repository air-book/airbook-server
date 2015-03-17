from django.db import models

from django.contrib.auth.models import User
from books.models import Book

class WishItem(models.Model):
    user = models.ForeignKey(User)
    book = models.ForeignKey(Book)


class CartItem(models.Model):
    user = models.ForeignKey(User)
    book = models.ForeignKey(Book)


