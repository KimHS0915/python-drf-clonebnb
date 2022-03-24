from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from .serializers import ReadUserSerializer, WriteUserSerializer


class MeView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = ReadUserSerializer(request.user)
        return Response(serializer.data)

    def put(self, request):
        serializer = WriteUserSerializer(request.user, data=request.data, partial=True)
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
            serializer = ReadUserSerializer(user)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
