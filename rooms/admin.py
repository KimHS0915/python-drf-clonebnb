from django.contrib import admin
from django.utils.html import mark_safe
from . import models


class PhotoInline(admin.TabularInline):

    model = models.Photo


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    """ Room Admin Definition """

    inlines = (PhotoInline,)
    fieldsets = (
        ('Basic Info', {
            'fields': (
                'name',
                'description',
                'country',
                'city',
                'address',
                'price',
                'room_type',
                'latitude',
                'longitude',
            ),
        }),
        ('Times', {
            'fields': (
                'check_in', 
                'check_out', 
                'instant_book',
            ),
        }),
        ('Spaces', {
            'fields': (
                'guests', 
                'beds', 
                'bedrooms', 
                'baths',
            ),
        }),
        ('More About the Space', {
            'classes': (
                'collapse',
            ),
            'fields': (
                'amenities', 
                'facilities', 
                'house_rules',
            ),
        }),
        ('Last details', {
            'fields': (
                'host',
            ),
        }),
    )
    
    
    list_display = (
        'name',
        'country',
        'city',
        'price',
        'address',
        'guests',
        'beds',
        'bedrooms',
        'baths',
        'check_in',
        'check_out',
        'instant_book',
        'count_amenities',
        'count_photos',
        'get_average_rating',
    )

    list_filter = (
        'instant_book',
        'host__superhost',
        'room_type',
        'amenities',
        'facilities',
        'house_rules',
        'city',
        'country',
    )

    raw_id_fields = ('host',)

    search_fields = ('=city', '^host__username')

    filter_horizontal = (
        'amenities',
        'facilities',
        'house_rules',
    )

    def count_amenities(self, obj):
        return obj.amenities.count()

    count_amenities.short_description = 'Amenity Count'

    def count_photos(self, obj):
        return obj.photos.count()
    
    count_photos.short_description = 'Photo Count'


@admin.register(models.RoomType, models.Amenity, models.Facility, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):
    """ Item Admin Definition """
    
    list_display = (
        'name',
        'used_by',
    )

    def used_by(self, obj):
        return obj.rooms.count()


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """ Photo Admin Definition """
    
    list_display = ('__str__', 'get_thumbnail')

    def get_thumbnail(self, obj):
        thumbnail = mark_safe(f'<img width="30px" src="{obj.file.url}" />')
        return thumbnail

    get_thumbnail.short_description = 'Thumbnail'