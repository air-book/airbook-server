from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from .serializers import ( BookShopSerializer, BookSerializer, 
    BookCategorySerializer, BookAuthorSerializer, BookImageSerializer )
from .models import BookShop, Book, BookCategory, BookAuthor, BookImage
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
import django_filters
from rest_framework import permissions 
from rest_framework.response import Response

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


class BooksAdminPermission(permissions.BasePermission):
    """
    
    """

    def has_permission(self, request, view):
        u = request.user
        try:
            bs = request.user.bookshop        
            return True
        except ObjectDoesNotExist:
            return False
        

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return obj.bookshop == request.user.bookshop


class BookAdminViewSet(BookViewSet):
    permission_classes=(permissions.IsAuthenticated, BooksAdminPermission, )

    def get_queryset(self):
        return Book.objects.filter(bookshop__user=self.request.user)

    def create(self, request):
        bs = request.user.bookshop
        data = request.data
        print request.data
        data['bookshop'] = bs.id
        serializer = BookSerializer(data=data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)


