from django.core import validators
from django.core.exceptions import ValidationError
from django.db import models


def validate_name(value):
    if not value.isalpha():
        raise ValidationError('Ensure this value contains only letters.')


def validate_image_size(value):
    max_size = value * 1024 * 1024
    if value > max_size:
        raise ValidationError('Max file size is 5.00 MB')


class Profile(models.Model):
    first_name = models.CharField(
        max_length=15,
        validators=(
            validators.MinLengthValidator(2),
            validate_name,
        )
    )

    last_name = models.CharField(
        max_length=15,
        validators=(
            validators.MinLengthValidator(2),
            validate_name,
        )
    )

    budget = models.FloatField(
        default=0,
        validators=(
            validators.MinValueValidator(0),
        )
    )

    profile_image = models.ImageField(
        blank=True,
        null=True,
        default='/static/images/user.png',
        validators=(
            validate_image_size,
        ),
    )


class Expense(models.Model):
    title = models.CharField(
        max_length=30,
    )

    expense_image = models.URLField()

    description = models.TextField(
        blank=True,
        null=True,
    )

    price = models.FloatField()
