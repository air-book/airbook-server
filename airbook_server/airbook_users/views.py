from .serializers import UserSerializer
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import APIException, AuthenticationFailed
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

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