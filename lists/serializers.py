from rest_framework import serializers
from .models import List
from users.serializers import UserSerializer


class ListSerializer(serializers.ModelSerializer):

    user = UserSerializer()
    
    class Meta:
        model = List
        fields = '__all__'