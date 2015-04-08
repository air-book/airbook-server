from django.conf.urls import patterns, include, url
from rest_framework.authtoken.views import ObtainAuthToken 
from .views import SessionLoginView, CurrentUserView, WishItemViewSet, CartItemViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'wishes', WishItemViewSet, base_name='wishes')
router.register(r'cart', CartItemViewSet, base_name='cart')

urlpatterns = patterns('',
    url(r'^token-auth/$', ObtainAuthToken.as_view()),
    url(r'^session-auth/$', SessionLoginView.as_view()),
    url(r'^me/$', CurrentUserView.as_view()),
    url(r'^', include(router.urls)),
)

