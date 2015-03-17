from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import WishItem, CartItem
from books.serializers import BookSerializer


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'groups', 'is_staff']


class WishItemSerializer(ModelSerializer):
    book_object = SerializerMethodField(read_only=True)

    def get_book_object(self,obj):
        return BookSerializer(obj.book).data

    class Meta:
        model = WishItem


class CartItemSerializer(ModelSerializer):
    class Meta:
        model = CartItem