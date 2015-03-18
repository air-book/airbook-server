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
from .serializers import WishItemSerializer
from .models import WishItem
from rest_framework import status
from books.models import Book


from rest_framework import permissions

class SameUserPermission(permissions.BasePermission):
    """
    
    """

    def has_object_permission(self, request, view, obj):
        print 1
        raise
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        #if request.method in permissions.SAFE_METHODS:
        #    return True

        # Instance must have an attribute named `owner`.
        print obj.user, request.user
        return obj.user == request.user
        #return False


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
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


"""
class WishItemViewSet(viewsets.ModelViewSet):
    serializer_class = WishItemSerializer
    permission_classes = (SameUserPermission,)

    def get_queryset(self):
        return WishItem.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        print serializer.istance
        serializer.save()


    def perform_update(self, serializer):
        instance = serializer.save()
        
"""
class WishItemViewSet(viewsets.GenericViewSet):
    model = WishItem
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated,)
    serializer_class = WishItemSerializer
    
    def get_queryset(self):
        return WishItem.objects.filter(user=self.request.user.id)

    def create(self, request):
        book = Book.objects.get(pk=request.data['book'])
        wish = WishItem.objects.create(user=request.user, book=book)
        return Response(status=status.HTTP_204_NO_CONTENT)
        
        
    def retrieve(self, request, pk=None):
        pass

    def destroy(self, request, pk=None, format=None):
        book = Book.objects.get(pk=pk)
        wish = WishItem.objects.filter(user=request.user, book=book)
        wish.delete()
        return Response({})


    







