import jwt
from django.conf import settings
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer


class UserSignupView(APIView):
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            new_user = serializer.save()
            return Response(UserSerializer(new_user).data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if not username or not password:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        user = authenticate(username=username, password=password)
        if user is not None:
            encoded_jwt = jwt.encode({'pk': user.pk}, settings.SECRET_KEY, algorithm='HS256')
            return Response(data={'token': encoded_jwt})
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


class MeView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    def put(self, request):
        serializer = UserSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailView(APIView):
    
    def get(self, request, *args, **kwargs):
        try:
            pk = self.kwargs['pk']
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
