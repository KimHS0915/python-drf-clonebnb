from rest_framework import serializers
from users.serializers import UserSerializer
from lists.models import List
from .models import Room, RoomType, Amenity, Facility, HouseRule


class RoomTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = RoomType
        fields = ('id', 'name')


class AmenitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Amenity
        fields = ('id', 'name')


class FacilitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Facility
        fields = ('id', 'name')


class HouseRuleSerializer(serializers.ModelSerializer):

    class Meta:
        model = HouseRule
        fields = ('id', 'name')


class RoomSerializer(serializers.ModelSerializer):

    host = UserSerializer(read_only=True)
    room_type = RoomTypeSerializer(read_only=True, required=False)
    amenities = AmenitySerializer(read_only=True, many=True, required=False)
    facilities = FacilitySerializer(read_only=True, many=True, required=False)
    house_rules = HouseRuleSerializer(read_only=True, many=True, required=False)
    is_fav = serializers.SerializerMethodField()

    class Meta:
        model = Room
        fields = '__all__'
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
