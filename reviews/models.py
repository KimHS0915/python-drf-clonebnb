from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from common.models import AbstractTimeStampedModel

class Review(AbstractTimeStampedModel):
    """ Review Model Definition """

    review = models.TextField()
    accuracy = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(1)])
    communication = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(1)])
    cleanliness = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(1)])
    location = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(1)])
    check_in = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(1)])
    value = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(1)])
    user = models.ForeignKey(
        'users.User', related_name='reviews', on_delete=models.CASCADE)
    room = models.ForeignKey(
        'rooms.Room', related_name='reviews', on_delete=models.CASCADE)
