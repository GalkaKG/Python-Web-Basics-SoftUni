from django.core.exceptions import ValidationError


def validate_min_characters_username(value):
    if value < 2:
        raise ValidationError('The username must be a minimum of 2 chars')


def validate_year(value):
    if not 1980 <= value <= 2049:
        ValidationError('Year must be between 1980 and 2049')
