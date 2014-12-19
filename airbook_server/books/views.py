from django.shortcuts import render
from .serializers import BookShopSerializer, BookSerializer
from .models import BookShop, Book
from rest_framework import viewsets


class BookShopViewSet(viewsets.ModelViewSet):
    serializer_class = BookShopSerializer
    queryset = BookShop.objects.all()

class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
