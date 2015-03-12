from django.conf.urls import patterns, include, url
from rest_framework.authtoken.views import ObtainAuthToken 
from .views import SessionLoginView, CurrentUserView


urlpatterns = patterns('',
    url(r'^token-auth/$', ObtainAuthToken.as_view()),
    url(r'^session-auth/$', SessionLoginView.as_view()),
    url(r'^me/$', CurrentUserView.as_view())
)

