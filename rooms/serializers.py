from rest_framework import serializers
from users.serializers import UserSerializer
from .models import Room

class RoomSerializer(serializers.ModelSerializer):

    host = UserSerializer()
    class Meta:
        model = Room
        fields = ('name', 'price', 'instant_book', 'host')
