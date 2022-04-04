from rest_framework.viewsets import ModelViewSet
from .permissions import IsGuest, IsRoomOwner
from .models import Reservation
from .serializers import ReservationSerializer


class ReservationViewSet(ModelViewSet):

    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def get_permissions(self):
        permission_classes = [IsGuest | IsRoomOwner]
        return [permission() for permission in permission_classes]
