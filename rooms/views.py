from rest_framework.generics import RetrieveAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Room
from .serializers import ReadRoomSerializer, WriteRoomSerializer


@api_view(['GET', 'POST'])
def room_list(request):
    if request.method == 'GET':
        rooms = Room.objects.all()
        serializer = ReadRoomSerializer(rooms, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        if not request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        serializer = WriteRoomSerializer(data=request.data)
        if serializer.is_valid():
            room = serializer.save(host=request.user)
            data = ReadRoomSerializer(room).data
            return Response(data=data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors,  status=status.HTTP_400_BAD_REQUEST)


class RoomDetailView(RetrieveAPIView):

    queryset = Room.objects.all()
    serializer_class = ReadRoomSerializer