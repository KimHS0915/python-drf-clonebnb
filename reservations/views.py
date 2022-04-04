from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, AllowAny
from .permissions import IsGuest, IsRoomOwner
from .models import Reservation
from .serializers import ReservationSerializer


class ReservationViewSet(ModelViewSet):

    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action == 'list' or self.action == 'update':
            permission_classes = [IsGuest]
        elif self.action == 'retrieve':
            permission_classes == [IsGuest | IsRoomOwner]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

    def list(self, request, *args, **kwargs):
        queryset = Reservation.objects.filter(guest=request.user)
        queryset = self.filter_queryset(queryset)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(page, many=True)
        return Response(serializer.data)   
