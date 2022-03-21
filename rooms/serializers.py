from rest_framework import serializers
from users.serializers import UserSerializer
from django_countries.serializer_fields import CountryField
from .models import Room

class ReadRoomSerializer(serializers.ModelSerializer):

    host = UserSerializer()
    class Meta:
        model = Room
        fields = '__all__'


class WriteRoomSerializer(serializers.Serializer):

    name = serializers.CharField(max_length=140)
    description = serializers.CharField(max_length=500)
    country = CountryField()
    city = serializers.CharField(max_length=80)
    price = serializers.IntegerField()
    address = serializers.CharField(max_length=140)
    guests = serializers.IntegerField()
    beds = serializers.IntegerField()
    bedrooms = serializers.IntegerField()
    baths = serializers.IntegerField()
    check_in = serializers.TimeField()
    check_out = serializers.TimeField()
    instant_book = serializers.BooleanField(default=False)
    lat = serializers.DecimalField(max_digits=10, decimal_places=6)
    lng = serializers.DecimalField(max_digits=10, decimal_places=6)

    def create(self, validated_data):
        return Room.objects.create(**validated_data)

    def validate(self, data):
        check_in = data.get('check_in')
        check_out = data.get('check_out')
        if check_in == check_out:
            raise serializers.ValidationError('Not enough time between changes')
        else:
            return data
