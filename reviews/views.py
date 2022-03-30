from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rooms.models import Room
from .models import Review
from .serializers import ReadReviewSerializer, WriteReviewSerializer


@api_view(['GET', 'POST'])
def room_reviews(request, pk):

    if request.method == 'GET':
        room = Room.objects.get(pk=pk)
        reviews = Review.objects.filter(room=room)
        serializer = ReadReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        if not request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        serializer = WriteReviewSerializer(data=request.data)
        if serializer.is_valid():
            room = Room.objects.get(pk=pk)
            review = serializer.save(user=request.user, room=room)
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors,  status=status.HTTP_400_BAD_REQUEST)
