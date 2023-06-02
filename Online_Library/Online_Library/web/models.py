from django.db import models


class Profile(models.Model):
    MAX_LENGTH = 30

    first_name = models.CharField(
        max_length=MAX_LENGTH,
    )

    last_name = models.CharField(
        max_length=MAX_LENGTH,
    )

    image_url = models.URLField()


class Book(models.Model):
    MAX_LENGTH = 30

    title = models.CharField(
        max_length=MAX_LENGTH,
    )

    description = models.TextField()

    image = models.URLField()

    type = models.CharField(
        max_length=MAX_LENGTH,
    )
