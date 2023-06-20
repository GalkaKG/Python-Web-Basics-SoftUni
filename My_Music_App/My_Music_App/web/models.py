from django.core import validators
from django.core.exceptions import ValidationError
from django.db import models
import re


def validate_username(username):
    pattern = r'^\w+$'
    match = re.match(pattern, username)
    if not match:
        raise ValidationError('Ensure this value contains only letters, numbers, and underscore.')


class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        validators=(
            validators.MinLengthValidator(2),
            validate_username,
        ),
    )

    email = models.EmailField()

    age = models.PositiveIntegerField(
        blank=True,
        null=True,
    )


class Album(models.Model):
    CHOICES = (
        ('POP MUSIC', 'Pop Music'),
        ('JAZZ MUSIC', 'Jazz Music'),
        ('R&B MUSIC', 'R&B Music'),
        ('ROCK MUSIC', 'Rock Music'),
        ('COUNTRY MUSIC', 'Country Music'),
        ('DANCE MUSIC', 'Dance Music'),
        ('HIP HOP MUSIC', 'Hip Hop Music'),
        ('OTHER', 'Other'),
    )

    album_name = models.CharField(
        unique=True,
        max_length=30,
        verbose_name='Album Name',
    )

    artist = models.CharField(
        max_length=30,
    )

    genre = models.CharField(
        max_length=30,
        choices=CHOICES,
    )

    description = models.TextField(
        blank=True,
        null=True,
    )

    image_url = models.URLField(
        verbose_name='Image URL',
    )

    price = models.FloatField(
        validators=(
            validators.MinValueValidator(0.0, 'The price cannot be below 0.0'),
        ),
    )
