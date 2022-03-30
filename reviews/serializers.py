from rest_framework import serializers
from users.serializers import UserSerializer
from .models import Review


class ReadReviewSerializer(serializers.ModelSerializer):

    user = UserSerializer()

    class Meta:
        model = Review
        fields = '__all__'


class WriteReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = (
            'review',
            'accuracy',
            'communication',
            'cleanliness',
            'location',
            'check_in',
            'value',
        )