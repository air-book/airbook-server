from .serializers import UserSerializer
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import APIException, AuthenticationFailed
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import mixins
from .serializers import WishItemSerializer, CartItemSerializer
from .models import WishItem, CartItem
from rest_framework import status
from books.models import Book


from rest_framework import permissions

class SameUserPermission(permissions.BasePermission):
    """
    --- Not used right now
    """

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class SessionLoginView(APIView):
    def post(self, request):
        if(request.user.id):
            serializer = UserSerializer(request.user)
            return Response(serializer.data)
        try:
            username = request.data['username']
            password = request.data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    #login(request, user)
                    serializer = UserSerializer(user)
                    return Response(serializer.data)

            raise AuthenticationFailed

        except:
            raise AuthenticationFailed



class CurrentUserView(APIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


class WishItemViewSet(viewsets.GenericViewSet):
    model = WishItem
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )
    serializer_class = WishItemSerializer

    def get_queryset(self):
        return WishItem.objects.filter(user=self.request.user.id)

    def create(self, request):
        book = Book.objects.get(pk=request.data['book'])
        wish = WishItem.objects.create(user=request.user, book=book)
        return Response(WishItemSerializer(wish, context={'request': request}).data)


    def destroy(self, request, pk=None, format=None):
        book = Book.objects.get(pk=pk)
        wish = WishItem.objects.filter(user=request.user, book=book)
        wish.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def list(self, request):
        queryset = self.get_queryset()
        serializer = WishItemSerializer (queryset, many=True, context={'request': request})
        return Response(serializer.data)



class CartItemViewSet(viewsets.GenericViewSet):
    model = CartItem
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )
    serializer_class = CartItemSerializer

    def get_queryset(self):
        return CartItem.objects.filter(user=self.request.user.id)

    def create(self, request):
        book = Book.objects.get(pk=request.data['book'])
        wish = CartItem.objects.create(user=request.user, book=book)
        return Response(CartItemSerializer(wish, context={'request': request}).data)


    def destroy(self, request, pk=None, format=None):
        book = Book.objects.get(pk=pk)
        wish = CartItem.objects.filter(user=request.user, book=book)
        wish.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def list(self, request):
        queryset = self.get_queryset()
        serializer = CartItemSerializer (queryset, many=True, context={'request': request})
        return Response(serializer.data)
