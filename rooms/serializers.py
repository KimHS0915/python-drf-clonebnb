from rest_framework import serializers
from users.serializers import UserSerializer
from lists.models import List
from .models import Room

class RoomSerializer(serializers.ModelSerializer):

    host = UserSerializer(read_only=True)
    is_fav = serializers.SerializerMethodField()

    class Meta:
        model = Room
        exclude = ('amenities', 'room_type', 'facilities', 'house_rules')
        read_only_fields = ('host', 'id', 'created', 'updated')

    def validate(self, data):
        if self.instance:
            check_in = data.get('check_in', self.instance.check_in)
            check_out = data.get('check_out', self.instance.check_out)
        else:
            check_in = data.get('check_in')
            check_out = data.get('check_out')
        if check_in == check_out:
            raise serializers.ValidationError('Not enough time between changes')
        return data

    def get_is_fav(self, obj):
        user = self.context.get('user')
        if user is not None and user.is_authenticated:
            lst = List.objects.get(user=user)
            return obj in lst.rooms.all()
        return False

    def create(self, validated_data):
        request = self.context.get('request')
        room = Room.objects.create(**validated_data, host=request.user)
        return room
