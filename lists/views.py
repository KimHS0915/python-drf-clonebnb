from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rooms.models import Room
from .models import List
from .serializers import ListSerializer


class ListView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        lst = List.objects.get(user=request.user)
        serializer = ListSerializer(lst)
        return Response(serializer.data)

    def put(self, request):
        pk = request.data.get('pk', None)
        user = request.user
        if pk is not None:
            try:
                lst = List.objects.get(user=request.user)
                room = Room.objects.get(pk=pk)
                print(lst.rooms.all())
                if room in lst.rooms.all():
                    lst.rooms.remove(room)
                else:
                    lst.rooms.add(room)
                return Response()
            except Room.DoesNotExist:
                pass
        return Response(status=status.HTTP_400_BAD_REQUEST)
