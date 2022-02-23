from django.db import models
from common.models import AbstractTimeStampedModel


class Conversation(AbstractTimeStampedModel):
     """ Conversation Model Definition """

     participants = models.ManyToManyField(
         'users.User', related_name='conversation', blank=True
     )


class Message(AbstractTimeStampedModel):
    """ Message Model Definition """

    message = models.TextField()
    user = models.ForeignKey(
        'users.User', related_name='messages', on_delete=models.CASCADE
    )
    Conversation = models.ForeignKey(
        'Conversation', related_name='messages', on_delete=models.CASCADE
    )
