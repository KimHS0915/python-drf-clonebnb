from django.db import models
from django_countries.fields import CountryField
from common.models import AbstractTimeStampedModel



class AbstractItem(AbstractTimeStampedModel):
    """ Abstract Item Definition """

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):
    """ RoomType Model Definition """

    class Meta:
        verbose_name = 'Room Type'


class Amenity(AbstractItem):
    """ Amenity Model Definition """

    class Meta:
        verbose_name_plural = 'Amenities'


class Facility(AbstractItem):
    """ Facility Model Definition """

    class Meta:
        verbose_name_plural = 'Facilities'


class HouseRule(AbstractItem):
    """ HouseRule Model Definition """

    class Meta:
        verbose_name = 'House Rule'


class Photo(AbstractTimeStampedModel):
    """ Photo Model Definition """

    caption = models.CharField(max_length=80)
    file = models.ImageField(upload_to='room_photos')
    room = models.ForeignKey(
        'Room', related_name='photos', on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


class Room(AbstractTimeStampedModel):
    """ Room Model Definitions """

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey(
        "users.User", related_name='rooms', on_delete=models.CASCADE)
    room_type = models.ForeignKey(
        "RoomType", related_name='rooms', on_delete=models.SET_NULL, null=True)
    amenities = models.ManyToManyField(
        "Amenity", related_name='rooms', blank=True)
    facilities = models.ManyToManyField(
        "Facility", related_name='rooms', blank=True)
    house_rules = models.ManyToManyField(
        "HouseRule", related_name='rooms', blank=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=6, null=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=6, null=True)

    def __str__(self):
        return self.name

    def get_average_rating(self):
        all_reviews = self.reviews.all()
        if not all_reviews:
            return ''
        all_ratings = 0
        for review in all_reviews:
            all_ratings += review.get_average_rating()
        return round(all_ratings / len(all_reviews), 2)

    get_average_rating.short_description = 'Average'

    class Meta:
        ordering = ('-created',)