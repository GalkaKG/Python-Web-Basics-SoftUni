from django.core.exceptions import ValidationError


def validate_first_letter_is_upper(value):
    if not value[0].isupper():
        raise ValidationError('The name must start with a capital letter.')


def validate_name_contains_only_letters(value):
    if not value.isaplha():
        raise ValidationError('Plant name should contain only letters!')