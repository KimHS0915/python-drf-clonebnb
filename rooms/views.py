from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from .models import Room
from .serializers import RoomSerializer


class RoomListView(APIView):

    def get(self, request):
        paginator = PageNumberPagination()
        paginator.page_size = 10
        rooms = Room.objects.all()
        results = paginator.paginate_queryset(rooms, request)
        serializer = RoomSerializer(results, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        if not request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            room = serializer.save(host=request.user)
            data = RoomSerializer(room).data
            return Response(data=data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors,  status=status.HTTP_400_BAD_REQUEST)


class RoomDetailView(APIView):

    def get_room(self, pk):
        try:
            room = Room.objects.get(pk=pk)
            return room
        except Room.DoesNotExist:
            return None

    def get(self, request, pk):
        room = self.get_room(pk)
        if room is not None:
            serializer = RoomSerializer(room)
            return Response(data=serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        room = self.get_room(pk)
        if room is not None:
            if room.host != request.user and not request.user.is_superuser:
                return Response(status=status.HTTP_403_FORBIDDEN)
            room.delete()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        room = self.get_room(pk)
        if room is not None:
            if room.host != request.user and not request.user.is_superuser:
                return Response(status=status.HTTP_403_FORBIDDEN)
            serializer = RoomSerializer(room, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(RoomSerializer(room).data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class RoomSearchView(APIView):

    def get(self, request):
        country = request.GET.get('country', None)
        city = request.GET.get('city', None)
        max_price = request.GET.get('max_price', None)
        min_price = request.GET.get('min_price', None)
        max_guests = request.GET.get('max_guests', None)
        min_guests = request.GET.get('min_guests', None)
        max_beds = request.GET.get('max_beds', None)
        min_beds = request.GET.get('min_beds', None)
        max_bedrooms = request.GET.get('max_bedrooms', None)
        min_bedrooms = request.GET.get('min_bedrooms', None)
        max_baths = request.GET.get('max_baths', None)
        min_baths = request.GET.get('min_baths', None)
        filter_kwargs = {}
        if country is not None:
            filter_kwargs['country'] = country
        if city is not None:
            filter_kwargs['city'] = city
        if max_price is not None:
            filter_kwargs['price__lte'] = max_price
        if min_price is not None:
            filter_kwargs['price__gte'] = min_price
        if max_guests is not None:
            filter_kwargs['guests__lte'] = max_guests
        if min_guests is not None:
            filter_kwargs['guests__gte'] = min_guests
        if max_beds is not None:
            filter_kwargs['beds__lte'] = max_beds
        if min_beds is not None:
            filter_kwargs['beds__gte'] = min_beds
        if max_bedrooms is not None:
            filter_kwargs['bedrooms__lte'] = max_bedrooms
        if min_bedrooms is not None:
            filter_kwargs['bedrooms__gte'] = min_bedrooms
        if max_baths is not None:
            filter_kwargs['baths__lte'] = max_baths
        if min_baths is not None:
            filter_kwargs['baths__gte'] = min_baths
        paginator = PageNumberPagination()
        paginator.page_size = 10
        try:
            rooms = Room.objects.filter(**filter_kwargs)
        except ValueError:
            rooms = Room.objects.all()
        results = paginator.paginate_queryset(rooms, request)
        serializer = RoomSerializer(results, many=True)
        return paginator.get_paginated_response(serializer.data)
