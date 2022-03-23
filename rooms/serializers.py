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
        if self.instance:
            check_in = data.get('check_in', self.instance.check_in)
            check_out = data.get('check_out', self.instance.check_out)
        else:
            check_in = data.get('check_in')
            check_out = data.get('check_out')
        if check_in == check_out:
            raise serializers.ValidationError('Not enough time between changes')
        return data

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.country = validated_data.get('country', instance.country)
        instance.city = validated_data.get('city', instance.city)
        instance.price = validated_data.get('price', instance.price)
        instance.address = validated_data.get('address', instance.address)
        instance.guests = validated_data.get('guests', instance.guests)
        instance.beds = validated_data.get('beds', instance.beds)
        instance.bedrooms = validated_data.get('bedrooms', instance.bedrooms)
        instance.baths = validated_data.get('baths', instance.baths)
        instance.check_in = validated_data.get('check_in', instance.check_in)
        instance.check_out = validated_data.get('check_out', instance.check_out)
        instance.instant_book = validated_data.get('instant_book', instance.instant_book)
        instance.lat = validated_data.get('lat', instance.lat)
        instance.lng = validated_data.get('lng', instance.lng)
        instance.save()
        return instance
