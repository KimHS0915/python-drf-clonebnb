from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet
from .models import List
from .serializers import ListSerializer


class ListViewSet(ModelViewSet):

    queryset = List.objects.all()
    serializer_class = ListSerializer

    def get_permissions(self):
        permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]
