from django.core.exceptions import ValidationError
from django.db import models


def validate_ingredients_separated_by_comma(ingredients):
    ingredients_res = ingredients.strip().split(',')
    error_message = 'The ingredients should be separated by ","'
    if len(ingredients_res) <= 1:
        raise ValidationError(error_message)


class Recipe(models.Model):
    title = models.CharField(max_length=30,)

    image_url = models.URLField()

    description = models.TextField()

    ingredients = models.CharField(
        max_length=250,
        validators=(validate_ingredients_separated_by_comma,),
    )

    time = models.IntegerField()

    def ingredients_list(self):
        return self.ingredients.split(',')
