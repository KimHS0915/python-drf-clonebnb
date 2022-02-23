from django.db import models
from common.models import AbstractTimeStampedModel


class List(AbstractTimeStampedModel):
    """ List Model Definition """

    name = models.CharField(max_length=80)
    user = models.OneToOneField(
        'users.User', related_name='list', on_delete=models.CASCADE)
    rooms = models.ManyToManyField(
        'rooms.Room', related_name='lists', blank=True)

    def __str__(self):
        return self.name