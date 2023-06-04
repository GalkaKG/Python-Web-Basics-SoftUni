from django.db import models


class ProfileModel(models.Model):
    MAX_LEN = 20

    first_name = models.CharField(max_length=MAX_LEN,)

    last_name = models.CharField(max_length=MAX_LEN,)

    age = models.IntegerField()

    image_url = models.URLField()


class NoteModel(models.Model):
    MAX_LEN = 30

    title = models.CharField(max_length=MAX_LEN,)

    image_url = models.URLField()

    content = models.TextField()

