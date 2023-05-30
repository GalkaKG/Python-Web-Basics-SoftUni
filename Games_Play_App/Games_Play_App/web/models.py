from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models


def rating_validate(value):
    if not 0.1 <= value <= 5.0:
        raise ValidationError('The rating can be between 0.1 and 5.0 (both inclusive)')


class ProfileModel(models.Model):
    MIN_AGE = 12
    MAX_LEN = 30

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.IntegerField(
        null=False,
        blank=False,
        validators=(
            MinValueValidator(MIN_AGE),
        ),
    )

    password = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_LEN,
    )

    first_name = models.CharField(
        null=True,
        blank=True,
        max_length=MAX_LEN,
    )

    last_name = models.CharField(
        null=True,
        blank=True,
        max_length=MAX_LEN,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )


class GameModel(models.Model):
    MAX_TITLE_LEN = 30
    MAX_CATEGORY_LEN = 15
    MIN_LEVEL = 1

    CHOICES = (
        ('ACTION', 'Action'),
        ('ADVENTURE', 'Adventure'),
        ('PUZZLE', 'Puzzle'),
        ('STRATEGY', 'Strategy'),
        ('SPORTS', 'Sports'),
        ('BOARD/CARD GAME', 'Board/Card Game'),
        ('OTHER', 'Other'),
    )

    title = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_TITLE_LEN,
        unique=True,
    )

    category = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_CATEGORY_LEN,
        choices=CHOICES,
    )

    rating = models.FloatField(
        null=False,
        blank=False,
        validators=(
            rating_validate,
        ),
    )

    max_level = models.IntegerField(
        null=True,
        blank=True,
        validators=(
            MinValueValidator(MIN_LEVEL),
        ),
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    summary = models.TextField(
        null=True,
        blank=True,
    )
