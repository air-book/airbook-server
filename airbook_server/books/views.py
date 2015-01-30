from django.shortcuts import render
from .serializers import ( BookShopSerializer, BookSerializer, 
    BookCategorySerializer, BookAuthorSerializer, BookImageSerializer )
from .models import BookShop, Book, BookCategory, BookAuthor, BookImage
from rest_framework import viewsets


class BookShopViewSet(viewsets.ModelViewSet):
    serializer_class = BookShopSerializer
    queryset = BookShop.objects.all()

class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BookCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = BookCategorySerializer
    queryset = BookCategory.objects.all()


class BookAuthorViewSet(viewsets.ModelViewSet):
    serializer_class = BookAuthorSerializer
    queryset = BookAuthor.objects.all()


class BookImageViewSet(viewsets.ModelViewSet):
    serializer_class = BookImageSerializer
    queryset = BookImage.objects.all()