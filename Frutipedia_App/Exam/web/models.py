from django.core import validators
from django.core.exceptions import ValidationError
from django.db import models


def validate_profile_name(value):
    if not value[0].isalpha():
        raise ValidationError('Your name must start with a letter!')


def validate_fruit_name(value):
    if not value.isalpha():
        raise ValidationError('Fruit name should contain only letters!')


class ProfileModel(models.Model):
    first_name = models.CharField(
        max_length=25,
        validators=(
            validators.MinLengthValidator(2),
            validate_profile_name,
        ),
        verbose_name='First Name'
    )

    last_name = models.CharField(
        max_length=35,
        validators=(
            validators.MinLengthValidator(1),
            validate_profile_name,
        ),
        verbose_name='Last Name',
    )

    email = models.EmailField(
        max_length=40,
    )

    password = models.CharField(
        max_length=20,
        validators=(
            validators.MinLengthValidator(8),
        ),
    )

    image_url = models.URLField(
        blank=True,
        null=True,
        verbose_name='Image URL'
    )

    age = models.PositiveIntegerField(
        blank=True,
        null=True,
        default=18,
    )


class FruitModel(models.Model):
    name = models.CharField(
        max_length=30,
        validators=(
            validators.MinLengthValidator(2),
            validate_fruit_name,
        ),
    )

    image_url = models.URLField(
        verbose_name='Image URL'
    )

    description = models.TextField()

    nutrition = models.TextField(
        blank=True,
        null=True,
    )
