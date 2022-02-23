from django.db import models
from .managers import CustomModelManager


class AbstractTimeStampedModel(models.Model):
    """ Time Stamped Model """

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = CustomModelManager()

    class Meta:
        abstract = True
        