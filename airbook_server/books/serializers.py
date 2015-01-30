from .models import BookShop, Book, BookCategory, BookAuthor, BookImage
from rest_framework import serializers


class BookShopSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookShop




class BookCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = BookCategory



class BookAuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookAuthor


class BookImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookImage        


class BookSerializer(serializers.ModelSerializer):

    images = BookImageSerializer(many=True, read_only=True)

    class Meta:
        model = Book
