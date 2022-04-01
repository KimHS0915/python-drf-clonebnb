from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from rooms.permissions import IsUserRoom
from .models import Room
from .serializers import RoomSerializer


class RoomViewSet(ModelViewSet):
    
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def get_permissions(self):
        
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [permissions.AllowAny]

        elif self.action == 'create':
            permission_classes = [permissions.IsAuthenticated]
        
        else:
            permission_classes = [IsUserRoom]
        
        return [permission() for permission in permission_classes]

    @action(detail=False)
    def search(self, request):
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
        latitude = request.GET.get('latitude', None)
        longitude = request.GET.get('longitude', None)
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
        if latitude is not None and longitude is not None:
            filter_kwargs['latitude__lte'] = float(latitude) + 0.005
            filter_kwargs['latitude__gte'] = float(latitude) - 0.005
            filter_kwargs['longitude__lte'] = float(longitude) + 0.005
            filter_kwargs['longitude__gte'] = float(longitude) - 0.005
        paginator = self.paginator
        try:
            rooms = Room.objects.filter(**filter_kwargs)
        except ValueError:
            rooms = Room.objects.all()
        results = paginator.paginate_queryset(rooms, request)
        serializer = RoomSerializer(results, many=True)
        return paginator.get_paginated_response(serializer.data)
