from .models import BookShop, Book
from rest_framework import serializers


class BookShopSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookShop


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book

        