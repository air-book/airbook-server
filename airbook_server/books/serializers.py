from .models import BookShop, Book, BookCategory, BookAuthor, BookImage
from rest_framework import serializers
from airbook_users.models import WishItem
from smartfilefield import SmartFileField

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

    image = SmartFileField()
    image_thumb = serializers.SerializerMethodField(read_only=True)

    def get_image_thumb(self, obj):
        return obj.image_thumb.url

    class Meta:
        model = BookImage        


class BookSerializer(serializers.ModelSerializer):

    images = BookImageSerializer(many=True, read_only=True)
    bookshop_name = serializers.SerializerMethodField(read_only=True)
    authors = BookAuthorSerializer(many=True, read_only=True)
    categories = BookCategorySerializer(many=True, read_only=True)
    is_wished = serializers.SerializerMethodField(read_only=True)
    in_cart = serializers.SerializerMethodField(read_only=True)

    def get_bookshop_name(self, obj):
        return obj.bookshop.name

    def get_is_wished(self, obj):
        req = self.context['request']
        if not req.user.id:
            return False
        user = req.user
        return obj.wishitem_set.filter(user=user).exists()

    def get_in_cart(self, obj):
        req = self.context['request']
        if not req.user.id:
            return False
        user = req.user
        return obj.cartitem_set.filter(user=user).exists()

    class Meta:
        model = Book

