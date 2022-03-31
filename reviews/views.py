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
            return Response(ReadReviewSerializer(review).data)
        else:
            return Response(data=serializer.errors,  status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail(request, pk):

    def get_review(pk):
        try:
            review = Review.objects.get(pk=pk)
            return review
        except Review.DoesNotExist:
            return None

    if request.method == 'GET':
        review = get_review(pk)
        if review is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ReadReviewSerializer(review)
        return Response(serializer.data)

    elif request.method == 'PUT':
        review = get_review(pk)
        if review is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if review.user != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        serializer = WriteReviewSerializer(review, data=request.data, partial=True)
        if serializer.is_valid():
            review = serializer.save()
            return Response(ReadReviewSerializer(review).data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        review = get_review(pk)
        if review is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if review.user != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        review.delete()
        return Response(status=status.HTTP_200_OK)
