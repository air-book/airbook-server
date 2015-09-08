from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from .serializers import ( BookShopSerializer, BookSerializer, 
    BookCategorySerializer, BookAuthorSerializer, BookImageSerializer )
from .models import BookShop, Book, BookCategory, BookAuthor, BookImage
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
import django_filters
from rest_framework import permissions 
from rest_framework import filters 
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
    filter_backends = (filters.SearchFilter,)

    search_fields = ['name']


class BookImageViewSet(viewsets.ModelViewSet):
    serializer_class = BookImageSerializer
    queryset = BookImage.objects.all()


class BooksAdminPermission(permissions.BasePermission):
    """
    
    """

    def has_permission(self, request, view):
        u = request.user
        try:
            bs = request.user.bookshopuser        
            return True
        except RelatedObjectDoesNotExist:
            return False
        

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return obj.bookshop == request.user.bookshopuser.bookshop


class BookAdminViewSet(BookViewSet):
    permission_classes=(permissions.IsAuthenticated, BooksAdminPermission, )

    def get_queryset(self):
        #return Book.objects.all()
        bookshop = self.request.user.bookshopuser.bookshop
        print bookshop.id
        return Book.objects.filter(bookshop=bookshop.id)

    def create(self, request):
        bs = request.user.bookshopuser.bookshop
        data = request.data
        data['bookshop'] = bs.id
        serializer = BookSerializer(data=data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)


    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        #dirty hack for authors
        if 'authors' in request.data:
            authors_ids = []
            for author in request.data['authors']:
                authors_ids.append(author['id']) 

            #drop not needed
            to_keep = instance.authors.filter(pk__in=authors_ids).values_list('id', flat=True)
            to_drop = instance.authors.exclude(pk__in=authors_ids)
            
            for x in to_drop:
                instance.authors.remove(x)
            #add new
            to_create = [x for x in authors_ids if x not in to_keep ]
            for c in to_create:
                author = BookAuthor.objects.get(pk=c)
                instance.authors.add(author)
                

        return Response(serializer.data)


