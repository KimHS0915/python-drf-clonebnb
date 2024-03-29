from django.db import models
from common.models import AbstractTimeStampedModel


class Conversation(AbstractTimeStampedModel):
    """ Conversation Model Definition """

    participants = models.ManyToManyField(
         'users.User', related_name='conversation', blank=True
    )
    
    def __str__(self):
        usernames = []
        for user in self.participants.all():
            usernames.append(user.username)
        return ", ".join(usernames)
    
    def count_messages(self):
        return self.messages.count()

    count_messages.short_description = 'Number of Messages'

    def count_participants(self):
        return self.participants.count()
    
    count_participants.short_description = 'Number of Participants'     


class Message(AbstractTimeStampedModel):
    """ Message Model Definition """

    message = models.TextField()
    user = models.ForeignKey(
        'users.User', related_name='messages', on_delete=models.CASCADE
    )
    Conversation = models.ForeignKey(
        'Conversation', related_name='messages', on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.user} says: {self.message}'
