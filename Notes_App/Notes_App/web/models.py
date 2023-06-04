from django.db import models


class ProfileModel(models.Model):
    MAX_LEN = 20

    first_name = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_LEN,
    )

    last_name = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_LEN,
    )

    age = models.IntegerField(
        null=False,
        blank=False,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )


class NoteModel(models.Model):
    MAX_LEN = 30

    title = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_LEN,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    content = models.TextField(
        null=False,
        blank=False,
    )

