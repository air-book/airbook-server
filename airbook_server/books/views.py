from django.shortcuts import render
from .serializers import ( BookShopSerializer, BookSerializer, 
    BookCategorySerializer, BookAuthorSerializer, BookImageSerializer )
from .models import BookShop, Book, BookCategory, BookAuthor, BookImage
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
import django_filters

class BookShopViewSet(viewsets.ModelViewSet):
    serializer_class = BookShopSerializer
    queryset = BookShop.objects.all()

class BookFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(name="price", lookup_type='gte')
    max_price = django_filters.NumberFilter(name="price", lookup_type='lte')
    title_contains = django_filters.CharFilter(name="title", lookup_type='icontains')

    class Meta:
        model = Book
        fields = ['bookshop', 'min_price', 'max_price', 'title_contains']



class BookViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication, )
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    filter_class = BookFilter


class BookCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = BookCategorySerializer
    queryset = BookCategory.objects.all()


class BookAuthorViewSet(viewsets.ModelViewSet):
    serializer_class = BookAuthorSerializer
    queryset = BookAuthor.objects.all()


class BookImageViewSet(viewsets.ModelViewSet):
    serializer_class = BookImageSerializer
    queryset = BookImage.objects.all()