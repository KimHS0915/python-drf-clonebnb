from rest_framework import serializers
from users.serializers import UserSerializer
from .models import Room

class RoomSerializer(serializers.ModelSerializer):

    host = UserSerializer()
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
