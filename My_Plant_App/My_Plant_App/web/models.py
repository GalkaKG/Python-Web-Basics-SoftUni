from django.core import validators
from django.db import models
from My_Plant_App.web.validators.custom_validators import validate_first_letter_is_upper,\
    validate_name_contains_only_letters


class ProfileModel(models.Model):
    MAX_LEN_USERNAME = 10
    MIN_LEN_USERNAME = 2
    MAX_LEN_NAME = 20

    username = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_LEN_USERNAME,
        validators=(
            validators.MinLengthValidator(MIN_LEN_USERNAME),
        )
    )

    first_name = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_LEN_NAME,
        validators=(
            validate_first_letter_is_upper,
        ),
        verbose_name='First Name',
    )

    last_name = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_LEN_NAME,
        validators=(
            validate_first_letter_is_upper,
        ),
        verbose_name='Last Name'
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )


class PlantModel(models.Model):
    MAX_PLANT_CHARS = 14
    MIN_PLANT_CHARS = 2

    CHOICES = (
        ('OUTDOOR PLANTS', 'Outdoor Plants'),
        ('INDOOR PLANTS', 'Indoor Plants'),
    )

    plant_type = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_PLANT_CHARS,
        choices=CHOICES,
    )

    name = models.CharField(
        null=False,
        blank=False,
        validators=(
            validators.MinLengthValidator(MIN_PLANT_CHARS),
            validate_name_contains_only_letters,
        ),
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    description = models.TextField(
        null=False,
        blank=False,
    )

    price = models.FloatField(
        null=False,
        blank=False,
    )
