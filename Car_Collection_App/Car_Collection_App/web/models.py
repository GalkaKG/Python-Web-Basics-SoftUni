from django.core import validators
from django.db import models
from . import custom_validators


class Profile(models.Model):
    MAX_CHAR = 30
    MIN_AGE = 18

    username = models.CharField(
        null=False,
        blank=False,
        max_length=10,
        validators=(
            custom_validators.validate_min_characters_username,
        ),
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.IntegerField(
        null=False,
        blank=False,
        validators=(
            validators.MinValueValidator(18),
        ),
    )

    password = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_CHAR,
    )

    first_name = models.CharField(
        null=True,
        blank=True,
        max_length=MAX_CHAR,
    )

    last_name = models.CharField(
        null=True,
        blank=True,
        max_length=MAX_CHAR,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )


class Car(models.Model):
    MAX_CHARS_TYPE = 10
    MODEL_MAX_LEN = 20
    MODEL_MIN_LEN = 2
    MIN_PRICE = 1

    CHOICES = (
        ('SPORTS CAR', 'Spots Car'),
        ('PICKUP', 'Pickup'),
        ('CROSSOVER', 'Crossover'),
        ('MINIBUS', 'Minibus'),
        ('OTHER', 'Other'),
    )

    type = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_CHARS_TYPE,
        choices=CHOICES,
    )

    model = models.CharField(
        null=False,
        blank=False,
        max_length=MODEL_MAX_LEN,
        validators=(
            validators.MinLengthValidator(MODEL_MIN_LEN),
        ),
    )

    year = models.IntegerField(
        null=False,
        blank=False,
        validators=(
            custom_validators.validate_year,
        ),
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    price = models.FloatField(
        null=False,
        blank=False,
        validators=(
            validators.MinValueValidator(MIN_PRICE),
        ),
    )
