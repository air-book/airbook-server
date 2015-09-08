#from django.contrib.auth.models import User
from authtools.models import User
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import WishItem, CartItem
from books.serializers import BookSerializer


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'groups', 'is_staff']


class WishItemSerializer(ModelSerializer):
    book_object = SerializerMethodField(read_only=True)
    def get_book_object(self,obj):
        return BookSerializer(obj.book, context=self.context).data

    class Meta:
        model = WishItem


class CartItemSerializer(ModelSerializer):
    book_object = SerializerMethodField(read_only=True)
    def get_book_object(self,obj):
        return BookSerializer(obj.book, context=self.context).data

    class Meta:
        model = CartItem