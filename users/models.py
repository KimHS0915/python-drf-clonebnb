from django.db import models
from django.contrib.auth.models import AbstractUser
from django.shortcuts import reverse

class User(AbstractUser):
    """ Custom User Model Definition """

    GENDER_MALE = 'male'
    GENDER_FEMALE = 'female'
    GENDER_OTHER = 'other'

    GENDER_CHOICES = (
        (GENDER_MALE, 'Male'),
        (GENDER_FEMALE, 'Female'),
        (GENDER_OTHER, 'Other'),
    )

    LANGUAGE_ENGLISH = 'en'
    LANGUAGE_KOREAN = 'kr'

    LANGUAGE_CHOICES = (
        (LANGUAGE_ENGLISH, 'English'),
        (LANGUAGE_KOREAN, 'Korean'),
    )

    CURRENCY_USD = 'usd'
    CURRENCY_KRW = 'krw'

    CURRENCY_CHOICES = (
        (CURRENCY_USD, 'USD'),
        (CURRENCY_KRW, 'KRW'),
    )

    avatar = models.ImageField('avatar', upload_to='avatars', blank=True)
    gender = models.CharField(
        'gender', choices=GENDER_CHOICES, max_length=10, blank=True)
    bio = models.TextField('bio', blank=True)
    birthdate = models.DateField('birthdate', blank=True, null=True)
    language = models.CharField(
        'language', choices=LANGUAGE_CHOICES, max_length=2, blank=True)
    currency = models.CharField(
        'currency', choices=CURRENCY_CHOICES, max_length=3, blank=True)
    superhost = models.BooleanField('superhost', default=False)
 
