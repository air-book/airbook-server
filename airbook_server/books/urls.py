from django.conf.urls import patterns, include, url
from .views import ( BookShopViewSet, BookViewSet, BookCategoryViewSet, 
    BookAuthorViewSet, BookImageViewSet )
from rest_framework.routers import SimpleRouter

router = SimpleRouter()

router.register(r'bookshops', BookShopViewSet)
router.register(r'books', BookViewSet)
router.register(r'bookscategories', BookCategoryViewSet)
router.register(r'booksauthors', BookAuthorViewSet)
router.register(r'booksimages', BookImageViewSet)



urlpatterns =  patterns('',
    url(r'^', include(router.urls)),
    
)


