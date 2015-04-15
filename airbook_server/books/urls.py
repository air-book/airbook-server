from django.conf.urls import patterns, include, url
from .views import ( BookShopViewSet, BookViewSet, BookTagsViewSet, 
    BookAuthorViewSet, BookImageViewSet, BookAdminViewSet )
from rest_framework.routers import SimpleRouter

router = SimpleRouter()

router.register(r'bookshops', BookShopViewSet)
router.register(r'books', BookViewSet)
router.register(r'booksadmin', BookAdminViewSet)
router.register(r'bookscategories', BookTagsViewSet )
router.register(r'booksauthors', BookAuthorViewSet)
router.register(r'booksimages', BookImageViewSet)



urlpatterns =  patterns('',
    url(r'^', include(router.urls)),
    
)

