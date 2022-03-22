from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Room
from .serializers import ReadRoomSerializer, WriteRoomSerializer


class RoomListView(APIView):

    def get(self, request):
        rooms = Room.objects.all()
        serializer = ReadRoomSerializer(rooms, many=True)
        return Response(data=serializer.data)

    def post(self, request):
        if not request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        serializer = WriteRoomSerializer(data=request.data)
        if serializer.is_valid():
            room = serializer.save(host=request.user)
            data = ReadRoomSerializer(room).data
            return Response(data=data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors,  status=status.HTTP_400_BAD_REQUEST)


class RoomDetailView(APIView):

    def get(self, request, pk):
        try:
            room = Room.objects.get(pk=pk)
            serializer = ReadRoomSerializer(room)
            return Response(data=serializer.data)
        except Room.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
