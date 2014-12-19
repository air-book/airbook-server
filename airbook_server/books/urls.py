from django.conf.urls import patterns, include, url
from .views import BookShopViewSet, BookViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()

router.register(r'bookshops', BookShopViewSet)
router.register(r'books', BookViewSet)


urlpatterns =  patterns('',
    url(r'^', include(router.urls)),
    
)


