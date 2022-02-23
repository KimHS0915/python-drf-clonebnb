from django.db import models
from common.models import AbstractTimeStampedModel


class BetweenDay(AbstractTimeStampedModel):
    """ BetweenDay Model Definition """

    day = models.DateField()
    reservation = models.ForeignKey('Reservation', on_delete=models.CASCADE)


class Reservation(AbstractTimeStampedModel):
    """ Reservation Model Definition """

    STATUS_PENDING = 'pending'
    STATUS_CONFIRMED = 'confirmed'
    STATUS_CANCELED = 'canceled'
    STATUS_CHOICES = (
        (STATUS_PENDING, 'Pending'),
        (STATUS_CONFIRMED, 'Confirmed'),
        (STATUS_CANCELED, 'Canceled')
    )

    status = models.CharField(
        max_length=12, choices=STATUS_CHOICES, default=STATUS_PENDING
    )
    check_in = models.DateField()
    check_out = models.DateField()
    guest = models.ForeignKey(
        'users.User', related_name='reservations', on_delete=models.CASCADE
    )
    room = models.ForeignKey(
        'rooms.Room', related_name='reservations', on_delete=models.CASCADE
    )
